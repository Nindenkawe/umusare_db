from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *
from django.core.validators import RegexValidator

from django.core.exceptions import ValidationError

class CustomBaseSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        additional_validators = kwargs.pop('additional_validators', {})
        super().__init__(*args, **kwargs)
        self.set_validators(additional_validators)

    def set_validators(self, additional_validators):
        # Iterate through all fields in the serializer
        for field_name, field in self.fields.items():
            # Set allow_null=False for all fields to disallow null values
            field.allow_null = False

            # Optionally, add additional validators based on field name
            if field_name in additional_validators:
                field.validators.extend(additional_validators[field_name])

            # Add data type validation for certain fields
            if field_name == "age":
                field.validators.append(serializers.MinValueValidator(0))
                field.validators.append(serializers.MaxValueValidator(150))
            elif field_name == "email":
                field.validators.append(serializers.EmailValidator())
            elif field_name == "phone_number":
                field.validators.append(RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Invalid phone number"))

            # Add custom validation method for other good practices
            if field_name == "custom_field":
                field.validators.append(self.validate_custom_field)

    def validate_custom_field(self, value):
        # Custom validation method for 'custom_field'
        if value < 0:
            raise ValidationError("Value cannot be negative")

# Example usage:
# Define additional validators for specific fields
additional_validators = {
    "name": [RegexValidator(regex=r'^[\w-]+$', message="Name must contain only letters, numbers, or hyphens")]
}


class UserSerializer(CustomBaseSerializer):
    class Meta:
        model = User
        fields = '__all__'

class SubscriberSerializer(CustomBaseSerializer):
    class Meta:
        model = Subscriber
        fields = '__all__'

class ProviderSerializer(CustomBaseSerializer):
    class Meta:
        model = Provider
        fields = '__all__'

class CarSerializer(CustomBaseSerializer):
    class Meta:
        model = Car
        fields = '__all__'
        # Pass additional validators to the base serializer
        additional_validators = additional_validators

class Car_serviceSerializer(CustomBaseSerializer):
    class Meta:
        model = Car_services
        fields = '__all__'

class Book_DriverSerializer(CustomBaseSerializer):
    class Meta:
        model = Book_Driver
        fields = '__all__'
    additional_validators = additional_validators
class Proposed_insucoversSerializer(CustomBaseSerializer):
    class Meta:
        model = Proposed_insucovers
        fields = '__all__'


class Chauffeur_profileSerializer(CustomBaseSerializer):
    class Meta:
        model = Chauffeur_profile
        fields = '__all__'

class Mechanic_profileSerializer(CustomBaseSerializer):
    class Meta:
        model = Mechanic_profile
        fields = '__all__'

class Parkingfacility_profileSerializer(CustomBaseSerializer):
    class Meta:
        model = Parkingfacility_profile
        fields = '__all__'


class RoadAssistanceSerializer(CustomBaseSerializer):
    class Meta:
        model = RoadAssistance
        fields = '__all__'


class Ownership_TransferSerializer(CustomBaseSerializer):
    class Meta:
        model = Ownership_Transfer
        fields = '__all__'



class Vehicle_deregistrationSerializer(CustomBaseSerializer):
    class Meta:
        model = Vehicle_deregistration
        fields = '__all__'