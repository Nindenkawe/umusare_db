import json
from authlib.integrations.django_client import OAuth
from django.conf import settings
from django.shortcuts import redirect, render, reverse
from urllib.parse import quote_plus, urlencode
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth.models import User
from .serializers import *
from .models import *
from rest_framework.generics import get_object_or_404
from . import utils
from django.http import JsonResponse
import jwt
import requests

def verify_jwt(token):
    # Fetch JWKS from Auth0's JWKS endpoint
    jwks_url = "https://your-auth0-domain/.well-known/jwks.json"
    jwks_response = requests.get(jwks_url)
    jwks = jwks_response.json()

    # Decode JWT header to get the "kid" field
    header = jwt.get_unverified_header(token)
    kid = header.get("kid")

    # Find the public key matching the "kid" from JWKS
    public_key = None
    for key in jwks["keys"]:
        if key["kid"] == kid:
            public_key = jwt.algorithms.RSAAlgorithm.from_jwk(json.dumps(key))
            break

    if public_key:
        try:
            decoded_token = jwt.decode(token, public_key, algorithms=["RS256"])
            return decoded_token
        except jwt.ExpiredSignatureError:
            # Handle token expiration
            pass
        except jwt.JWTError:
            # Handle other JWT errors
            pass

    return None

def get_token_auth_header(request):
    """Obtains the Access Token from the Authorization Header
    """
    auth = request.META.get("HTTP_AUTHORIZATION", None)
    if auth:
        parts = auth.split()
        if parts[0].lower() == "bearer":
            if len(parts) == 2:
                return parts[1]
            else:
                response = JsonResponse({'message': 'Malformed authorization header'})
                response.status_code = 401
                return response
        else:
            response = JsonResponse({'message': 'Authorization header must start with "Bearer"'})
            response.status_code = 401
            return response
    else:
        response = JsonResponse({'message': 'Authorization header missing'})
        response.status_code = 401
        return response


# Initialize OAuth instance
oauth = OAuth()

oauth.register(
    "auth0",
    client_id=settings.AUTH0_CLIENT_ID,
    client_secret=settings.AUTH0_CLIENT_SECRET,
    client_kwargs={
        "scope": "openid profile email",
    },
    server_metadata_url=f"https://{settings.AUTH0_DOMAIN}/.well-known/openid-configuration",
)

# Constants
CALLBACK_URL = "car_services:callback"
INDEX_URL = "car_services:index"

def login(request):
    return oauth.auth0.authorize_redirect(
        request, request.build_absolute_uri(reverse(CALLBACK_URL))
    )

def callback(request):
    try:
        token = oauth.auth0.authorize_access_token(request)
        request.session["user"] = token
        return redirect(reverse(INDEX_URL))
    except Exception as e:
        # Handle error, redirect to an error page, or log the error
        return redirect(reverse(INDEX_URL)) 

def logout(request):
    request.session.clear()

    return redirect(
        f"https://{settings.AUTH0_DOMAIN}/v2/logout?"
        + urlencode(
            {
                "returnTo": request.build_absolute_uri(reverse(INDEX_URL)),
                "client_id": settings.AUTH0_CLIENT_ID,
            },
            quote_via=quote_plus,
        ),
    )
    
def index(request):
    return render(
        request,
        "index.html",
        context={
            "session": request.session.get("user"),
            "pretty": json.dumps(request.session.get("user"), indent=4),
        },
    )

class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class BaseAPIView(APIView):
    permission_classes = [IsAuthenticated|ReadOnly]
    model = None
    serializer_class = None

    def get_object(self, pk):
        return get_object_or_404(self.model, pk=pk)

    def get(self, request, pk=None, format=None):
        if pk:
            instance = self.get_object(pk)
            serializer = self.serializer_class(instance)
            return Response(serializer.data)
        else:
            instances = self.model.objects.all()
            serializer = self.serializer_class(instances, many=True)
            return Response(serializer.data)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {
                'message': f'{self.model.__name__} Created Successfully',
                'data': serializer.data
            },
            status=status.HTTP_201_CREATED
        )

    def put(self, request, pk=None, format=None):
        instance = self.get_object(pk)
        serializer = self.serializer_class(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {
                'message': f'{self.model.__name__} Updated Successfully',
                'data': serializer.data
            }
        )

    def delete(self, request, pk, format=None):
        instance = self.get_object(pk)
        instance.delete()
        return Response({'message': f'{self.model.__name__} Deleted Successfully'})

class LoadUserAPIView(BaseAPIView):
    permission_classes = [IsAuthenticated|ReadOnly]
    model = User
    serializer_class = UserSerializer

class SubscriberAPIView(BaseAPIView):
    model = Subscriber
    serializer_class = SubscriberSerializer

class ProviderAPIView(BaseAPIView):
    model = Provider
    serializer_class = ProviderSerializer

class TransactionAPIView(BaseAPIView):
    model = Transaction
    serializer_class = TransactionSerializer

class CarAPIView(BaseAPIView):
    model = Car
    serializer_class = CarSerializer

class Proposed_insucoversAPIView(BaseAPIView):
    model = Proposed_insucovers
    serializer_class = Proposed_insucoversSerializer

class Chauffeur_profileAPIView(BaseAPIView):
    model = Chauffeur_profile
    serializer_class = Chauffeur_profileSerializer

class Mechanic_profileAPIView(BaseAPIView):
    model = Mechanic_profile
    serializer_class = Mechanic_profileSerializer

class Book_DriverAPIView(BaseAPIView):
    model = Book_Driver
    serializer_class = Book_DriverSerializer

class Parkingfacility_profileAPIView(BaseAPIView):
    model = Parkingfacility_profile
    serializer_class = Parkingfacility_profileSerializer


class RoadAssistanceAPIView(BaseAPIView):
    model = RoadAssistance
    serializer_class = RoadAssistanceSerializer


class Ownership_TransferAPIView(BaseAPIView):
    model = Ownership_Transfer
    serializer_class = Ownership_TransferSerializer


class Vehicle_deregistrationAPIView(BaseAPIView):
    model = Vehicle_deregistration
    serializer_class = Vehicle_deregistrationSerializer
