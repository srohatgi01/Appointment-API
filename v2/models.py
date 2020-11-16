from django.db import models
import uuid

class User(models.Model):
    """This is the Users model where all users data will be saved"""
    uuid = models.CharField(default=uuid.uuid4, max_length=50, primary_key=True)
    first_name    = models.CharField(max_length=20)
    last_name     = models.CharField(max_length=20)
    email_id      = models.EmailField(max_length=100, default="")
    city          = models.CharField(max_length=20, blank=True)
    state         = models.CharField(max_length=50, blank=True)
    country       = models.CharField(max_length=20, blank=True)
    zip_code      = models.CharField(max_length=6, blank=True)
    mobile_number = models.CharField(max_length=10, blank=True)
    birthdate     = models.DateField(blank=True, null=True)
    photo_url     = models.URLField(max_length=255, blank=True)
    gender        = models.CharField(max_length=10, blank=True)
    joined        = models.DateTimeField(auto_now_add=True, blank=True, null=True)


    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Zorg(models.Model):
    """This is the Zorg model"""
    name               = models.CharField(max_length=100)
    unique_id          = models.EmailField(max_length=30, unique=True)
    owner_first_name   = models.CharField(max_length=20)
    owner_last_name    = models.CharField(max_length=20)
    salon_email_id     = models.EmailField(max_length=100)
    owner_email_id     = models.EmailField(max_length=100)
    open_year_of_salon = models.CharField(max_length=4)
    website            = models.URLField(max_length=100)
    base_rating        = models.IntegerField(default=2)
    profile_photo      = models.ImageField(upload_to='zorg/profile_photo/', null=True, blank=True, max_length=200)
    joined             = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    

    def __str__(self):
        return self.name

class Zorg_Branche(models.Model):
    zorg = models.ForeignKey(Zorg, on_delete=models.CASCADE,null=True, related_name="branches")
    address = models.CharField(max_length=255)
    city          = models.CharField(max_length=20, blank=True)
    state         = models.CharField(max_length=50, blank=True)
    country       = models.CharField(max_length=20, blank=True)
    zip_code      = models.CharField(max_length=6, blank=True)

    def __str__(self):
        return str(self.zorg) + '  '+ self.address
    
class Categories(models.Model):
    zorg = models.ForeignKey(Zorg, on_delete=models.CASCADE, null=True, related_name='categories')
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name  + ' - ' + str(self.zorg) 

class Service(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE,null=True, related_name='services')
    service_name = models.CharField(max_length=100)
    time = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False)

    def __str__(self):
        return self.service_name + ' in ' + str(self.category)
    
class Appointment_Status(models.Model):
    status = models.CharField(max_length=15)

    def __str__(self):
        return self.status


# Whenever the user make an appointment, one record will be stored in the "appointment" model but it will add
# as many records to the "AppointmentDetail" model as the number of services the user booked.
class Appointment(models.Model):
    """This is the model where all the orders/Appointments will be saved"""
    user        = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    zorg        = models.ForeignKey(Zorg, on_delete=models.CASCADE, null=True)
    branch      = models.ForeignKey(Zorg_Branche, on_delete=models.CASCADE,null=True, related_name='branch')
    timestamp   = models.DateTimeField(auto_now_add=True, blank=True)
    status      = models.ForeignKey(Appointment_Status, on_delete=models.CASCADE, null=True)
    totaltime   = models.PositiveIntegerField(default=0)
    total_price = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    

    def __str__(self):
        return  str(self.user) + ' -> '  + str(self.zorg)

class AppointmentDetail(models.Model):
    appointment  = models.ForeignKey(Appointment, on_delete=models.CASCADE,null=True, related_name='appointment')
    # category     = models.ForeignKey(Categories, on_delete=models.CASCADE,null=True, related_name='category')
    service      = models.ForeignKey(Service, on_delete=models.CASCADE,null=True, related_name='service')
    # servicePrice = models.DecimalField(max_digits=10, decimal_places=2)
    # discount     = models.DecimalField(max_digits=10, decimal_places=2, null=True, default=0)

    def __str__(self):
        return str(self.appointment) + '  ' + str(self.service)
    
class UserCoin(models.Model):
    """This model contains the amount of coin each user has"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    amount  = models.IntegerField()

    def __str__(self):
        return 'ID:' + self.user + ' ' +'AMT:' + str(self.amount) 

class Advertisment(models.Model):
    zorg  = models.ForeignKey(Zorg, on_delete=models.CASCADE, null=True)
    datetime = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    link     = models.URLField(max_length=255)

    def __str__(self):
        return str(self.zorg)


def sample_upload_path(instance, filename):
    return '/'.join(['sample', str(instance.title), filename])
     

class SampleModel(models.Model):
    text = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='sample_upload_path', null=True, blank=True)
    file = models.FileField(upload_to='files/', null=True, blank=True, max_length=200)