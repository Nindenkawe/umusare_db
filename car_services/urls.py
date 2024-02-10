from . import views
from django.urls import path
from .views import (
    LoadUserAPIView,
    SubscriberAPIView,
    CarAPIView,
    Proposed_insucoversAPIView,
    ProviderAPIView,
    Chauffeur_profileAPIView,
    Mechanic_profileAPIView,
    TransactionAPIView,
    Book_DriverAPIView,
    Parkingfacility_profileAPIView,
    RoadAssistanceAPIView,
    Ownership_TransferAPIView,
    Vehicle_deregistrationAPIView,
    Dashboard,
    home
)

urlpatterns = [
    # auth
    path("", views.index, name="index"),
    path("admin_dashboard", views.Dashboard, name="Dashboard"),
    path("home", views.home, name="Home"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("callback/", views.callback, name="callback"),

    #handle incoming requests
    path('user', LoadUserAPIView.as_view(), name="user"),
    path('user/<str:pk>', LoadUserAPIView.as_view(), name="user"),
    path('subscriber', SubscriberAPIView.as_view(), name="subscriber"),
    path('subscriber/<str:pk>', SubscriberAPIView.as_view(), name="subscriber"),
    path('car', CarAPIView.as_view(), name="car"),
    path('car/<str:pk>', CarAPIView.as_view(), name="car"),
    path('carinsurance', Proposed_insucoversAPIView.as_view(), name="carinsurance"),
    path('carinsurance/<str:pk>', Proposed_insucoversAPIView.as_view(), name="carinsurance"),
    path('provider', ProviderAPIView.as_view(), name="provider"),
    path('provider/<str:pk>', ProviderAPIView.as_view(), name="provider"),
    path('chauffeur', Chauffeur_profileAPIView.as_view(), name="chauffeur"),
    path('chauffeur/<str:pk>', Chauffeur_profileAPIView.as_view(), name="chauffeur"),
    path('mechanic', Mechanic_profileAPIView.as_view(), name="mechanic"),
    path('mechanic/<str:pk>', Mechanic_profileAPIView.as_view(), name="mechanic"),
    path('transaction', TransactionAPIView.as_view(), name="transaction"),
    path('transaction/<str:pk>', TransactionAPIView.as_view(), name="transaction"),
    path('book_Driver', Book_DriverAPIView.as_view(), name="book_Driver"),
    path('book_Driver/<str:pk>', Book_DriverAPIView.as_view(), name="book_Driver"),
    path('parking', Parkingfacility_profileAPIView.as_view(), name="parking"),
    path('parking/<str:pk>', Parkingfacility_profileAPIView.as_view(), name="parking"),
    path('roadAssistance', RoadAssistanceAPIView.as_view(), name="roadAssistance"),
    path('roadAssistance/<str:pk>', RoadAssistanceAPIView.as_view(), name="roadAssistance"),
    path('transfer', Ownership_TransferAPIView.as_view(), name="transfer"),
    path('transfer/<str:pk>', Ownership_TransferAPIView.as_view(), name="transfer"),
    path('deregistration', Vehicle_deregistrationAPIView.as_view(), name="deregistration"),
    path('deregistration/<str:pk>', Vehicle_deregistrationAPIView.as_view(), name="deregistration"),
]