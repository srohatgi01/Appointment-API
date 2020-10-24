from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter, SimpleRouter

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user-list')
router.register(r'zorgs', ZorgViewSet, basename='zorg-list')
router.register(r'appointments', AppointmentViewSet, basename='appointments')

urlpatterns = router.urls
