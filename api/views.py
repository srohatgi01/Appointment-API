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
from rest_framework import renderers
import json

# class UserGenericView(generics.GenericAPIView):
#     serializer_class = UserSerializer

#     def get_queryset(self):
#         email_id = self.kwargs['email_id']
#         return User.objects.filter(email_id=email_id)

# class UserRenderer(renderers.JSONRenderer):
#     '''
#     User Renderer Class
#     '''
#     charset = 'utf-8'

#     def render(self, data, accepted_media_type=None, renderer_context=None):
#         response = json.dumps(data)

#         return response

# class UserFilter(filters.FilterSet):
#     '''
#     User Filter Class
#     '''
#     class Meta: 
#         model = User
#         fields = {
#             'email_id': ['iexact']
#         }

# class UserModelViewSet(viewsets.ModelViewSet):
#     """
#     viewSet.ModelViewset
#     """
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
    # lookup_field = 'first_name'
    # filter_backends = [DjangoFilterBackend]
    # filterset_class = UserFilter
    # renderer_classes = [UserRenderer]

    
# class UserGenericView(generics.GenericAPIView):
#     def get_queryset(self):
#         return super().get_queryset()
    
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
        serializer = ZorgSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk):
        """
        This method returns the specific zorg you asked for using the pk
        """
        queryset = Zorg.objects.all()
        zorg = get_object_or_404(queryset, pk=pk)  
        serializer = ZorgSerializer(zorg)
        return Response(serializer.data)

    def create(self, request):
        """
        This method creates the new zorg entry
        """
        serializer = ZorgSerializer(data=request.data)

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