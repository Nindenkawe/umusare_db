from wsgiref import validate
import uuid
from django.db import models
from django.contrib.auth.models import User
from .utils import PhoneNumberField


class Subscriber(models.Model, PhoneNumberField):
	sub = models.OneToOneField(User,
        on_delete=models.SET_NULL,
        related_name="Subscriber",
        null=True,
    )
	phone_number = PhoneNumberField(blank=False)
	parking_wallet = models.IntegerField(default=0)
	Rewards = models.IntegerField(default=0)


	
	def __str__(self):
		return f"{self.phone_number}"

	def save(self, *args, **kwargs):
		self.phone_number = self.phone_number
		if self.phone_number == True:
			self.phone_number == validate
		super().save(*args, **kwargs)

class Car(models.Model):
	sub = models.OneToOneField(User,
	on_delete=models.CASCADE,
	related_name="Car",
	null=True,
	)
	#genre = models.CharField(max_length=64, null=True)
	tin_number = models.CharField(max_length=64, null=True)
	yellow_cardNumber = models.CharField
	plate_number = models.CharField(max_length=15, null=True)
	frame_number = models.CharField(max_length=20, null=True)
	engine_number = models.CharField(max_length=20, null=True)
	make_year = models.CharField(max_length=10, null=True)
	vehicule_model = models.CharField(max_length=64, null=True)
	number_of_seats = models.CharField(max_length=64, null=True)
	Horse_power = models.CharField(max_length=64, null=True)
	#Date_issued = models.DateField(default=None)
	use_of_vehicule_choice = (
	('Drive & Business', 'Drive & Business'),
	('Transport of goods', 'Transport of goods'),
	('Transport of Fuel', 'Transport of Fuel'),
	('Taxi', 'Taxi')
	)	
	use_of_vehicule = models.CharField(
	max_length=32,
	choices=use_of_vehicule_choice,)
	insurance_status = models.BooleanField(default=False)
	traffic_violations_status = models.BooleanField(default=False)
	motorvehicle_inspection_date = models.DateField(null=True)

	def __str__(self):
		return self.plate_number

	def save(self, *args, **kwargs):
		self.plate_number = self.plate_number
		if self.plate_number == True:
			self.plate_number == validate
		super().save(*args, **kwargs)

class Transaction(models.Model):
	sub = models.ForeignKey(User,
        on_delete=models.CASCADE,
        related_name="Transaction",
        null=True,
    )
	
	transaction_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

	Transaction_choice = (
	('E_Parking', 'Pay_parking'),
	('E_Insurance', 'Buy_insurance'),
	('Mechanical_serv', 'Book_mechanic'),
	('Chauffeur_4hire', 'Chauffeur_4hire')
	)
	Transaction_type = models.CharField(
	max_length=32,
	choices=Transaction_choice,)

	provider_id = models.CharField(max_length=15, null=True)
	amount = models.IntegerField(default=0)
	transaction_status = models.BooleanField(default=False)


	def __str__(self):
		return f"{self.transaction_id}"

	def confirm_transaction(self, *args, **kwargs):
		self.amount = self.amount
		if self.transaction_id == True:
			self.transaction_status == validate
		super().save(*args, **kwargs)

#make sure the Fkey here is the car's Pk
class Proposed_insucovers(models.Model):
	sub = models.OneToOneField(User,
	on_delete=models.CASCADE,
	related_name="Proposed_insucovers",
	null=True,
)
	Third_party_liabilityGuarantee = models.BooleanField(default=False)
	window_breaking = models.BooleanField(default=False)
	Recoure = models.BooleanField(default=False)
	material_damaged = models.BooleanField(default=False)
	Theft_Covers = models.BooleanField(default=False)
	Fire_Covers = models.BooleanField(
	default=False)
	Third_party_plus = models.BooleanField(default=False)
	Without_deductible = models.BooleanField(default=False)
	Only_Localy_coverd = models.BooleanField(
	default=False,)
	Towing_system = models.BooleanField(default=False)
	accident_hist4thelast2years = models.CharField(max_length=20)
	was_your_previous_policy_canceled = models.BooleanField(default=False)

	def __str__(self):
		return f"{self.sub}"


class Provider(models.Model):
	provider = models.OneToOneField(User,
	on_delete=models.CASCADE,
	related_name="Provider",
	null=True,
    )

	service_offered = (
	('E_Parking', 'E_Parking'),
	('E_Insurance', 'E_Insurance'),
	('Mechanical_serv', 'Mechanical_serv'),
	('Chauffeur_4hire', 'Chauffeur_4hire')
	)	
	service_type = models.CharField(
	max_length=32,
	choices=service_offered,)
	tin_number = models.IntegerField(default=0)
	
	def __str__(self):
		return f"{self.provider}"


class Chauffeur_profile(models.Model, PhoneNumberField):
	prov = models.OneToOneField(Provider,
			on_delete=models.CASCADE,
			related_name="Chauffeur_profile",
			null=True,
	)	
	name = models.CharField(max_length=64)
	rating = models.IntegerField(default=0)
	Avg_ETA = models.CharField(max_length=20)
	phone_number = PhoneNumberField(blank=False)
	driver_license = models.CharField(max_length=40)
	Provider_wallet = models.IntegerField(default=0)


	def __str__(self):
		return f"{self.prov}"


class Mechanic_profile(models.Model):
	prov = models.OneToOneField(Provider,
			on_delete=models.CASCADE,
			related_name="Mechanic_profile",
			null=True,
	)	
	rating = models.IntegerField(default=0)
	phone_number = PhoneNumberField(blank=False)
	driver_license_number = models.CharField(max_length=40)
	mechanical_cert = models.CharField(max_length=40)
	Provider_wallet = models.IntegerField(default=0)

	def __str__(self):
		return f"{self.prov}"


class Parkingfacility_profile(models.Model):
	prov = models.OneToOneField(Provider,
			on_delete=models.CASCADE,
			related_name="Parkingfacility_profile",
			null=True,
	)
	phone_number = PhoneNumberField(blank=False)
	building_capacity = models.CharField(max_length=40)
	min_fee = models.IntegerField(default=0)
	security_history = models.BooleanField(default=False)
	Provider_wallet = models.IntegerField(default=0)

	def __str__(self):
		return f"{self.prov}"


class RoadAssistance(models.Model):
	
	prov = models.OneToOneField(Provider,
		on_delete=models.CASCADE,
		related_name="RoadAssistance",
		null=True,)
	Assistanse_choice = (
	('Quick_chauffeur', 'Driver'),
	('Mechanical_consult', 'Mechanic'),
	('Accident_claim', 'Road_Assistance'),
	('Accident_Report', 'traffic/Medical_Assistance')
	)	
	Assistanse_type = models.CharField(
	max_length=32,
	choices=Assistanse_choice,)
	none_Ihuteuser = models.BooleanField(default=False)
	driver_license = models.CharField(max_length=15)
	location = models.CharField(max_length=20)
	date = models.DateField()
	time = models.TimeField()
	accident_description = models.CharField(max_length=100)
	accident_severity = models.CharField(max_length=20)
	accident_damage = models.CharField(max_length=20)
	accident_injury = models.CharField(max_length=20)
	accident_claim_status = models.BooleanField(default=False)
	accident_sitevisuals = models.FileField()
	is_driver_required = models.BooleanField(default=False)
	Is_mechanic_required = models.BooleanField(default=False)
	
	def __str__(self):
		return f"{self.prov}"
		

class Ownership_Transfer(models.Model):
	sub = models.OneToOneField(User,
		on_delete=models.CASCADE,
		related_name="Ownership_Transfer",
		null=True,)
	DOC_id = models.UUIDField(
		max_length = 10,
		blank=True,
		editable=False,
		unique=True,
		default=uuid.uuid4
	)
	Transfer_date = models.DateField(default=None)
	Reason_for_Transfer = (
		('Sale','Sale'),('Transfer','Transfer'),
		('Other','Other')
	)
	Reason_for_Transfer = models.CharField(
	max_length=32,
	choices=Reason_for_Transfer,)
	Buyer_Tin = models.CharField(max_length=50)
	Sticker_number = models.CharField
	Sticker_date = models.DateField
	yellow_cardNumber = models.CharField
	Fee = models.IntegerField

	def __str__(self):
		return f"{self.sub}"
	

class Book_Driver(models.Model):
	when_is_driver_needed = (
	('Quick_chauffeur', 'Now'),
	('Schedule', 'Later'),

	)
	when = models.CharField(
	max_length=32,
	choices=when_is_driver_needed,)

	contact_info = models.CharField(max_length=11)
	location = models.CharField(max_length=20)
	payment_status = models.BooleanField

	def __str__(self):
		return f"{self.contact_info}"
	


class Vehicle_deregistration(models.Model):
	sub = models.OneToOneField(User,
		on_delete=models.CASCADE,
		related_name="Vehicle_deregistration",
		null=True,)
	
	deregistration_date = models.DateField
	deregistration_choices = (
	('scrapped', 'scrapped'),
	('exportation', 'exportation'),
	('other', 'other')

	)
	deregistration_reason = models.CharField(
	max_length=32,
	choices=deregistration_choices,)
	yellow_cardNumber = models.CharField
	yellow_plateNumber = models.BooleanField
	white_plateNumber = models.BooleanField

	def __str__(self):
		return f"{self.deregistration_reason}"


""" class pay_fuel(models.Model):
	sub = models.OneToOneField(User, on_delete=models.CASCADE,related_name="pay_fuel", null=True)
	purchase_date = models.DateField
	petro_stations = (
		('SP', 'SP'),
		('Rubis','Rubis'),
		('Merez','Merez')
	)
	selected_station = models.CharField(
	max_length=32,
	choices=petro_stations,)
	price = models.AutoField(null=False)
 """