#These imports are commonly used when you are working 
# with Django's authentication system (using the 
# User model) and when defining serializers for your
# Django REST Framework API to handle data serialization
# and deserialization tasks effectively.

from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Note

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields= ["id", "username", "password"] 
        extra_kwargs = {"password": {"write_only": True}}

    def create(self,validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model= Note
        fields = ["id", "title", "content", "created_at", "author"]
        extra_Kwargds = {"author": {"read_only": True}}