from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, generics
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters
from rest_framework import renderers, pagination, mixins, filters
import json

# Create your views here.
class UserViewSet(viewsets.ViewSet):  
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
        

class ZorgResultsSetPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 10

class ZorgView(generics.ListAPIView, generics.CreateAPIView):
    queryset = Zorg.objects.all().order_by('?')
    serializer_class = ZorgSerializer
    pagination_class = ZorgResultsSetPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filter_fields = ['name']
    search_fields = ['^name']

    
# class ZorgViewSet(viewsets.ViewSet):
#     """
#     This viewset is for Zorg Serializer
#     """

#     def list(self, request):
#         """
#         This method returns all the zorgs saved in the database in JSON format
#         """
#         queryset = Zorg.objects.all()
#         # pagination.PageNumberPagination.page_size = 10
#         serializer = ZorgSerializer(queryset, many=True)
       
#         # pagination_class = ZorgResultsSetPagination
#         return Response(serializer.data)
    
#     def retrieve(self, request, pk):
#         """
#         This method returns the specific zorg you asked for using the pk
#         """
#         queryset = Zorg.objects.all()
#         zorg = get_object_or_404(queryset, pk=pk)  
#         serializer = ZorgSerializer(zorg)
#         return Response(serializer.data)

#     def create(self, request):
#         """
#         This method creates the new zorg entry
#         """
#         serializer = ZorgSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def update(self, request, pk):
#         """
#         """
#         pass
    
#     def destroy(self, request, pk):
#         """
#         """
#         pass

class AppointmentDetailViewSet(viewsets.ViewSet):
    """
    """

    def list(self, request):
        queryset = Categories.objects.all()
        serializer = AppointmentDetailSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = AppointmentDetailSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AppointmentViewSet(viewsets.ViewSet):
    """
    """

    def list(self, request):
        queryset = Appointment.objects.all()
        serializer = AppointmentSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        """
        """
        queryset = Appointment.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = AppointmentSerializer(user)
        return Response(serializer.data)

    def create(self, request):
        """
        This method creates the new service entry
        """
        serializer = AppointmentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

