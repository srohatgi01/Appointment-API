# from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
# from rest_framework.permissions import IsAuthenticated

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser

# All models
# from .models import User, Zorg, UserPhoto, UserCoin, Gender, Appointment_Status, Appointment, Advertisment, Zorg_Rating, AppointmentDetail, Service, Zorg_Branche, Categories
from .models import *

# All Serializers
# from .serilizers import  UserSerializer, ZorgSerilizer, CategorySerilizer, ServiceSerilizer, AppointmentSerilizer, AppointmentDetailSerilizer, GenderSerilizer, UserPhotoSerilizer, ZorgBranchSerilizer, AppointmentStatusSerilizer, UserCoinSerilizer, AdvertismentSerilizer, ZorgRatingSerilizer
from .serializers import *

# REST Framework Imports
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status, viewsets
from django.shortcuts import get_object_or_404

# class GetUsers(APIView):
#     def get(self, request):
#         users = User.objects.all()
#         serializer = GetUserSerializer(users, many = True)
#         return Response(serializer.data)

# class UserModelView(APIView):
#     def get(self, request):
#         users = User.objects.all()
#         serializer = UserModelSerializer(users, many = True)
#         return Response(serializer.data)

class UserViewSet(viewsets.ViewSet):
    """
    This is a proper viewset to use during api calls as of 12th September
    """

    def list(self, request):
        """
        """
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk):
        """
        """
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    def create(self, request):
        """
        """
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk):
        """
        """
        pass

    def destroy(self, request, pk):
        """
        """
        pass
        
# class GetUserDetails(APIView):
#     def get_object(self, id):
#         try:
#             return User.objects.get(id=id)
        
#         except User.DoesNotExist:
#             return HttpResponse(status=status.HTTP_404_NOT_FOUND)

#     def get(self, request, id):
#         user = self.get_object(id)
#         serializer = GetUserSerializer(user)
#         return Response(serializer.data)

#     def put(self, request, id):
#         user = self.get_object(id)
#         serializer = PutUserSerializer(user, data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, id):
#         user = self.get_object(id)
#         user.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# class CreateUser(APIView):
#     def post(self, request):
#         serializer = CreateUserSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# class GetUserDetails(APIView):
#     def get_object(self, id):
#         try:
#             return User.objects.get(id=id)
        
#         except User.DoesNotExist:
#             return HttpResponse(status=status.HTTP_404_NOT_FOUND)

#     def get(self, request, id):
#         user = self.get_object(id)
#         serializer = UserModelSerializer(user)
#         return Response(serializer.data)

#     def put(self, request, id):
#         user = self.get_object(id)
#         serializer = UserModelSerializer(user, data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, id):
#         user = self.get_object(id)
#         user.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

class ZorgViewSet(viewsets.ViewSet):
    """
    This viewset is for Zorg Serializer
    """

    def list(self, request):
        """
        This method returns all the zorgs saved in the database in JSON format
        """
        queryset = Zorg.objects.all()
        serializer = ZorgSerilizer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk):
        """
        This method returns the specific zorg you asked for using the pk
        """
        queryset = Zorg.objects.all()
        zorg = get_object_or_404(queryset, pk=pk)  
        serializer = ZorgSerilizer(zorg)
        return Response(serializer.data)

    def create(self, request):
        """
        This method creates the new zorg entry
        """
        serializer = ZorgSerilizer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        """
        """
        pass
    
    def destroy(self, request, pk):
        """
        """
        pass

class CategoryViewSet(viewsets.ViewSet):
    """
    """

    def list(self, request):
        queryset = Categories.objects.all()
        serializer = CategorySerilizer(queryset, many=True)
        return Response(serializer.data)