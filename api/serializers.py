from rest_framework import serializers
# from .models import User, Zorg, UserPhoto, UserCoin, Gender, Appointment_Status, Appointment, Advertisment, Zorg_Rating, AppointmentDetail, Service, Zorg_Branche, Categories
from .models import *

class GenderSerilizer(serializers.ModelSerializer):
    '''This is a general gender serializer'''
    class Meta:
        model = Gender
        exclude = [
                    'id',
                ]              

class UserSerializer(serializers.ModelSerializer):
    """
        A usable working user serializer
    """
    gender = GenderSerilizer()
    class Meta:
        model = User
        fields = [
                    'id',
                    'first_name',
                    'last_name',
                    'email_id',
                    'city',
                    'state',
                    'country',
                    'zip_code',
                    'mobile_number',
                    'birthdate',
                    'photo_url',
                    'gender',
                    
                ]

    def create(self, validated_data):
        # gender_data = validated_data.pop('gender')
        # gender = Gender.objects.get_or_create(**validated_data)
        # user = User(..., gender=gender_data)
        # User.objects.create(user = user, **gender_data)
        # return user
        gender = validated_data.pop('gender')
        gender_instance = Gender.objects.get(**gender)
        user = User.objects.create(gender=gender_instance, **validated_data)
        return user


# class GetUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         exclude = ['id'] 
#         depth = 1
      
# class CreateUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = '__all__'

# class PutUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model= User
#         exclude = ['email_id', 'joined']
class CategorySerializer(serializers.ModelSerializer):
    """
    """
    # zorg = ZorgSerilizer()
    class Meta:
        model = Categories
        fields = ['category_name',]

class ZorgSerializer(serializers.ModelSerializer):
    """
    This is a serializer for zorgs only.
    """
    categories = CategorySerializer(many=True)
    class Meta:
        model = Zorg
        fields = [
            'id',
            'name',
            'owner_first_name',
            'owner_last_name',
            'salon_email_id',
            'owner_email_id',
            'open_year_of_salon',
            'website',
            'base_rating',
            'categories',
        ]


        # depth = 1


class ServiceSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class AppointmentSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'

class AppointmentDetailSerilizer(serializers.ModelSerializer):
    class Meta:
        model = AppointmentDetail
        fields = '__all__'



class ZorgBranchSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Zorg_Branche
        fields = '__all__'

class AppointmentStatusSerilizer(serializers.ModelSerializer):

    class Meta:
        model = Appointment_Status
        fields = '__all__'

class UserCoinSerilizer(serializers.ModelSerializer):
    class Meta:
        model = UserCoin
        fields = '__all__'

class AdvertismentSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Advertisment
        fields = '__all__'

class ZorgRatingSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Zorg_Rating
        fields = '__all__'
