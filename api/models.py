from django.db import models


class Gender(models.Model):
    """This model contains all the available genders that users can choose to select"""
    gender = models.CharField(max_length=10)

    def __str__(self):
        return self.gender

class User(models.Model):
    """This is the Users model where all users data will be saved"""
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
    gender        = models.ForeignKey(Gender, on_delete=models.CASCADE, null=True, blank=True, related_name='user_gender')
    joined        = models.DateTimeField(auto_now_add=True, blank=True, null=True)


    def __str__(self):
        return self.first_name + ' ' + self.last_name

class UserPhoto(models.Model):
    """This model contains the URL for photo url of Users"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    link = models.URLField(max_length=255)

    def __str__(self):
        return str(self.user)

class Zorg(models.Model):
    """This is the Zorg model"""
    name               = models.CharField(max_length=100)
    owner_first_name   = models.CharField(max_length=20)
    owner_last_name    = models.CharField(max_length=20)
    salon_email_id     = models.EmailField(max_length=100)
    owner_email_id     = models.EmailField(max_length=100)
    open_year_of_salon = models.CharField(max_length=4)
    website            = models.URLField(max_length=100)
    base_rating        = models.IntegerField(default=2)
    joined             = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    

    def __str__(self):
        return self.name

class Zorg_Branche(models.Model):
    zorg = models.ForeignKey(Zorg, on_delete=models.CASCADE,null=True)
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
    category = models.ForeignKey(Categories, on_delete=models.CASCADE,null=True, related_name="services")
    zorg = models.ForeignKey(Zorg, on_delete=models.CASCADE,null=True, related_name="zorg")
    service_name = models.CharField(max_length=100)
    time = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False)

    def __str__(self):
        return self.service_name + ' in ' + str(self.category)
    
class Appointment_Status(models.Model):
    status = models.CharField(max_length=15)

    def __str__(self):
        return self.status

class Appointment(models.Model):
    """This is the model where all the orders/Appointments will be saved"""
    user        = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    zorg        = models.ForeignKey(Zorg, on_delete=models.CASCADE, null=True)
    timestamp   = models.DateTimeField(auto_now_add=True, blank=True)
    status      = models.ForeignKey(Appointment_Status, on_delete=models.CASCADE, null=True)
    totaltime   = models.PositiveIntegerField(default=0)
    total_price = models.DecimalField(decimal_places=2, max_digits=10)
    

    def __str__(self):
        return  str(self.user) + ' -> '  + str(self.zorg)

class AppointmentDetail(models.Model):
    appointment  = models.ForeignKey(Appointment, on_delete=models.CASCADE,null=True)
    branch       = models.ForeignKey(Zorg_Branche, on_delete=models.CASCADE,null=True)
    category     = models.ForeignKey(Categories, on_delete=models.CASCADE,null=True)
    service      = models.ForeignKey(Service, on_delete=models.CASCADE,null=True)
    servicePrice = models.DecimalField(max_digits=10, decimal_places=2)
    discount     = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    def __str__(self):
        return str(self.appointment) + '  ' + str(self.branch) + '  ' + str(self.service)
    
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
     
class Zorg_Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    zorg = models.ForeignKey(Zorg, on_delete=models.CASCADE,null=True)
    # appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE,null=True)
    rating = models.IntegerField()

    def __str__(self):
        return self.zorg + ' ' + self.user