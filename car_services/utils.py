from django.core.exceptions import ValidationError
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from django.conf import settings
from django.db import models
import phonenumbers
import requests
import json
import jwt
import sys

AUTH0_DOMAIN = settings.AUTH0_DOMAIN

def jwt_decode_token(token):
    header = jwt.get_unverified_header(token)
    jwks = requests.get(f'https://{AUTH0_DOMAIN}/.well-known/jwks.json', timeout=5).json()  # Set timeout to 5 seconds
    public_key = None
    print("**********************************************************************{}", file=sys.stderr)

    for jwk in jwks['keys']:
        string_kid = header.get('kid')
        print(header.get('kid'), file=sys.stderr)
        print(jwk['kid'], file=sys.stderr)
        if jwk['kid'] == string_kid:
            print("**********************************************************************{}".format(string_kid), file=sys.stderr)
            public_key = jwt.algorithms.RSAAlgorithm.from_jwk(json.dumps(jwk))
            break  # No need to continue once public_key is found

    if public_key is None:
        raise Exception('Public key not found for the given kid.')

    issuer = f'https://{AUTH0_DOMAIN}/'
    return jwt.decode(token, public_key, audience='umusare', issuer=issuer, algorithms=['RS256'])

def jwt_get_username_from_payload_handler(payload):
    username = payload.get('sub', '').replace('|', '.')
    if username:
        authenticate(remote_user=username)
    return username

class PhoneNumberField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 10  # Adjust the max length as needed
        super().__init__(*args, **kwargs)

    def validate(self, value, model_instance):
        super().validate(value, model_instance)
        try:
            parsed_number = phonenumbers.parse(value, None)
            if not phonenumbers.is_valid_number(parsed_number):
                raise ValidationError('Invalid phone number format')
        except phonenumbers.NumberParseException:
            raise ValidationError('Invalid phone number')

    def get_prep_value(self, value):
        # Ensure the stored value is in E.164 format
        parsed_number = phonenumbers.parse(value, None)
        return phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)



class MTNMoMoPaymentView(APIView):
    def __init__(self, payeeNote, externalId, amount, currency, subscriber):
        self.payeeNote = payeeNote
        self.externalId = externalId
        self.amount = amount
        self.currency = currency
        self.payer = Payer(partyIdType="MSISDN", partyId=subscriber.phone_number)  # Assuming Payer class defined elsewhere

        if not self.payer.partyId.isdigit() or len(self.payer.partyId) != 10:
            raise ValidationError("Invalid phone number format. Must be 10-digit number.")

    def to_dict(self):
        return {
            "payeeNote": self.payeeNote,
            "externalId": self.externalId,
            "amount": self.amount,
            "currency": self.currency,
            "payer": self.payer.dict(),
        }
    def post(self, request):
        """
        Initiate a mobile money payment using MTN MoMo API.
        """

        # Get data from request
        serializer = PaymentRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        payment_request = serializer.save()

        # Authentication token for the MoMo API (replace with your actual token)
        auth_token = "your_auth_token_here"

        # Construct headers
        headers = {
            "Content-Type": "application/json",
            "Ocp-Apim-Subscription-Key": "FFtw@Lz@6qWR83W",
            "Authorization": f"Bearer {auth_token}"
        }

        # Convert PaymentRequest to dictionary
        data = payment_request.dict()

        # Make request to MoMo API
        try:
            response = requests.post("https://sandbox.momodeveloper.mtn.com/collection/v2_0/requesttowithdraw", headers=headers, json=data, timeout=5)
            response.raise_for_status()  # Raise exception for non-200 status codes
        except requests.exceptions.RequestException as e:
            raise HTTPException(status_code=500, detail=f"Error: {e}")

        # Handle successful response (202 Accepted)
        if response.status_code == 202:
            return Response({"message": "Payment request accepted"})
        else:
            # Handle unexpected errors (should ideally be logged)
            raise HTTPException(status_code=500, detail="Unknown error occurred")
