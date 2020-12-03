from django.shortcuts import render,redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import *
from .forms import RegistrationForm
from rest_framework import viewsets,status,generics
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework.permissions import IsAuthenticated
from .serializer import *
from .permissions import IsAdminOrReadOnly
# Create your views here.


class AdminProfileList(APIView):
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


    
# class HoodList(APIView):
#     def get(self, request, format=None):
#         all_hood = Neighborhood.objects.all()
#         serializers = NeighSerializer(all_hood, many=True)
#         return Response(serializers.data)

# class ResidentList(APIView):
#     def get(self, request, format=None):
#         all_resident = ResidentProfile.objects.all()
#         serializers = ResidentSerializer(all_resident, many=True)
#         return Response(serializers.data)

# class BusinessList(APIView):
#     def get(self, request, format=None):
#         all_business = Business.objects.all()
#         serializers = BusinessSerializer(all_business, many=True)
#         return Response(serializers.data)


class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = UserSignupSerializer
    queryset = User.objects.all()
