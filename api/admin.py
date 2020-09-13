from django.contrib import admin

# Register your models here.
from .models import User, Zorg, UserPhoto, UserCoin, Gender, Appointment_Status, Appointment, Advertisment, Zorg_Rating, AppointmentDetail, Service, Zorg_Branche, Categories

# Register your models here.


admin.site.register(User)
admin.site.register(Zorg)
admin.site.register(UserPhoto)
admin.site.register(UserCoin)
admin.site.register(Gender)
admin.site.register(Appointment_Status)
admin.site.register(Appointment)
admin.site.register(Advertisment)
admin.site.register(Zorg_Rating)
admin.site.register(AppointmentDetail)
admin.site.register(Service)
admin.site.register(Zorg_Branche)
admin.site.register(Categories)