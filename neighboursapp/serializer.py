
from rest_framework import serializers
from .models import *

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = HoodadminProfile
        fields = ('admin', 'prof_picture', 'bio')

class HoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = NeighbourHood
        fields = ('name', 'location', 'admin','hoodphoto','body','residents','emergency_contact')

class ResidentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resident
        fields = ('user', 'name','bio', 'profile_pic','hoodname','contact')

class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = ('name', 'body','email','neighbourhood','location')

class UserSignupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff', 'password']

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(UserSerializer, self).create(validated_data)