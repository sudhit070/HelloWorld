from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet
from .views import ContactApi


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', include('rest_framework.urls', namespace='rest_framework')),
    path('contact', ContactApi.as_view(), name="Contact"),
]

