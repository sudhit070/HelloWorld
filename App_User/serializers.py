from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import ContactQuery

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']



class ContactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ContactQuery
        fields = ['email', 'related', 'subject', 'message']