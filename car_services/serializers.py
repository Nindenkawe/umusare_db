from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = '__all__'

class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = '__all__'

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'

class Book_DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book_Driver
        fields = '__all__'

class Proposed_insucoversSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proposed_insucovers
        fields = '__all__'


class Chauffeur_profileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chauffeur_profile
        fields = '__all__'

class Mechanic_profileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mechanic_profile
        fields = '__all__'

class Parkingfacility_profileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parkingfacility_profile
        fields = '__all__'


class RoadAssistanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoadAssistance
        fields = '__all__'


class Ownership_TransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ownership_Transfer
        fields = '__all__'



class Vehicle_deregistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle_deregistration
        fields = '__all__'
