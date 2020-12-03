from django.shortcuts import render,redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import *
from .forms import RegistrationForm
from rest_framework import viewsets,status,generics
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework.permissions import IsAuthenticated
from .serializer import HoodSerializer,AdminSerializer,ResidentsSerializer,BusinessSerializer
# Create your views here.


class ProfileList(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get(self,request,format=None):
        all_profiles = HoodadminProfile.objects.all()
        serializers = ProfileSerializer(all_profiles,many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = HoodSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


   