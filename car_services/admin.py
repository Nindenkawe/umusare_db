from django.contrib import admin
from .models import *


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    pass

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    pass

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    pass

@admin.register(Book_Driver)
class Book_DriverAdmin(admin.ModelAdmin):
    pass

@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    pass

@admin.register(Chauffeur_profile)
class Chauffeur_profileAdmin(admin.ModelAdmin):
    pass

@admin.register(Mechanic_profile)
class Mechanic_profileAdmin(admin.ModelAdmin):
    pass

@admin.register(Proposed_insucovers)
class Proposed_insucoversAdmin(admin.ModelAdmin):
    pass

@admin.register(Parkingfacility_profile)
class Parkingfacility_profileAdmin(admin.ModelAdmin):
    pass


@admin.register(RoadAssistance)
class RoadAssistanceAdmin(admin.ModelAdmin):
    pass

@admin.register(Ownership_Transfer)
class Ownership_TransferAdmin(admin.ModelAdmin):
    pass

