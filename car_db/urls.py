from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path(f"{settings.APP_NAME}/", include(("car_services.urls", "car_services"))),
]
