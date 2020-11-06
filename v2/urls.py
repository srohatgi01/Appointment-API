from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user-list')
router.register(r'appointments', AppointmentViewSet, basename='appointments')

# # Should be uncommented when Zorg's viewsets.Viewset view is used in views.py
# router.register(r'zorgs', ZorgViewSet, basename='zorg-list')

# # This should be used if only viewset based views are used.
# urlpatterns = router.urls

# # Using this because it includes class based urls and viewset based urls.
urlpatterns = [path('zorgs/', ZorgView.as_view(), name='zorg-list')] + router.urls