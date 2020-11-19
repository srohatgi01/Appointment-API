from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    """
        A usable working user serializer
    """
    # gender = GenderSerilizer()

    class Meta:
        model = User
        fields = [
                    'uuid',
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

    # def create(self, validated_data):
    #     gender = validated_data.pop('gender')
    #     gender_instance = Gender.objects.get(**gender)
    #     user = User.objects.create(gender=gender_instance, **validated_data)
    #     return user

class ZorgBranchSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Zorg_Branche
        exclude = ['id', 'zorg']

class ServiceSerializer(serializers.ModelSerializer):
    """
    This is a serializer to serializer and deserailize service serailizer.
    """
    class Meta:
        model = Service
        exclude = ['id', 'category']

class CategorySerializer(serializers.ModelSerializer):
    """
    This serailizer is to serialize and deserailize category model
    """
    services = ServiceSerializer(many=True)
    class Meta:
        model = Categories
        fields = ['category_name', 'services']

    # def create(self, validated_data):
    #     services = validated_data.pop('services')
    #     print(services)
    #     categories = Categories.objects.create(**validated_data)
    #     for service in services:
    #         Service.objects.create(category=categories, **service)
    #     return categories

class ZorgSerializer(serializers.ModelSerializer):
    """
    This is a serializer for zorgs only.
    """
    branches = ZorgBranchSerilizer(many=True)
    categories = CategorySerializer(many=True)
    class Meta:
        model = Zorg
        fields = [
            'id',
            'unique_id',
            'name',
            'owner_first_name',
            'owner_last_name',
            'salon_email_id',
            'owner_email_id',
            'open_year_of_salon',
            'website',
            'profile_photo',
            'cover_photo',
            'photo_1',
            'photo_2',
            'photo_3',
            'photo_4',
            'base_rating',
            'branches',
            'categories',
        ]


    def create(self, validated_data):
        branches = validated_data.pop('branches')
        categories = validated_data.pop('categories')
        zorg = Zorg.objects.create(**validated_data)
        for category in categories:
            services = category.pop('services')
            category = Categories.objects.create(zorg=zorg, **category)
            
            for service in services:
                Service.objects.create(category=category, **service)
        for branch in branches:
            Zorg_Branche.objects.create(zorg=zorg, **branch)
        return zorg

class UserAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
                    'id',
                    'first_name',
                    'last_name',
                    'email_id',
                    'mobile_number',
                    'birthdate',
                    'photo_url',
                    'gender',
                  ]

class ZorgBranchAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zorg_Branche
        exclude = ['id', 'zorg']

class ServiceAppointmentSerializer(serializers.ModelSerializer):
    """
    This is a serializer to serializer and deserailize service serailizer.
    """
    # category = CategoryAppointmentSerializer()
    class Meta:
        model = Service
        exclude = ['id', 'category']

class ZorgAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zorg
        fields = [
                    'id',
                     'name',
                     'salon_email_id',
                     'website'
                 ]

class AppointmentDetailSerializer(serializers.ModelSerializer):

    service = ServiceAppointmentSerializer()
    class Meta:
        model = AppointmentDetail
        exclude = ['id', 'appointment']

class AppointmentStatusSerilizer(serializers.ModelSerializer):

    class Meta:
        model = Appointment_Status
        fields = ['status']

class AppointmentSerializer(serializers.ModelSerializer):
    appointment = AppointmentDetailSerializer(many=True)
    status = AppointmentStatusSerilizer()
    user = UserAppointmentSerializer()
    zorg = ZorgAppointmentSerializer()
    branch = ZorgBranchAppointmentSerializer()
    class Meta:
        model = Appointment
        fields = [
                'id', 
                'status',
                'appointment',
                'user',
                'zorg',
                'branch',
                'timestamp',
                'totaltime',
                'total_price'
            ]

    def create(self, validated_data):
        user = validated_data.pop('user')
        zorg = validated_data.pop('zorg')
        status = validated_data.pop('status')
        branch = validated_data.pop('branch')

        user_instance = User.objects.get(**user)
        zorg_instance = Zorg.objects.get(**zorg)
        status_instance = Appointment_Status.objects.get(**status)
        branch_instance = Zorg_Branche.objects.get(**branch)

        appointment_services = validated_data.pop('appointment')

        appointment = Appointment.objects.create(user = user_instance, zorg = zorg_instance, status = status_instance, branch = branch_instance, **validated_data)

        for services in appointment_services:
            service = services.pop('service')
            service_instance = Service.objects.get(**service)
            AppointmentDetail.objects.create(appointment=appointment, service=service_instance)

        return appointment

class UserCoinSerilizer(serializers.ModelSerializer):
    class Meta:
        model = UserCoin
        fields = '__all__'

class AdvertismentSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Advertisment
        fields = '__all__'
