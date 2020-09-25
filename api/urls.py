from django.urls import path
# from rest_framework import routers

# from .views import GetUsers, GetUserDetails, CreateUser, UserModelView

# urlpatterns = [
#     # To list all the users
#     path('api/v1/users/', GetUsers.as_view()), 
#     # To list one particular user given the id of that user
#     path('api/v1/user/<int:id>/', GetUserDetails.as_view()),
#     # To create a new user  
#     path('api/v1/users/createuser/', CreateUser.as_view()),
#     # UserModelView
#     path('api/v1/users/usermodelview/', UserModelView.as_view()),
# ]
# from .views import UserViewSet, ZorgViewSet, CategoryViewSet
from .views import *
from rest_framework.routers import DefaultRouter, SimpleRouter

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user-list')
router.register(r'zorgs', ZorgViewSet, basename='zorg-list')
router.register(r'app-details', AppointmentDetailViewSet, basename='app-details')
router.register(r'appointments', AppointmentViewSet, basename='appointments')
# router.register(r'services', ServiceViewSet, basename='service-list')
urlpatterns = router.urls