from .models import Reserve, PostAttachment, Specialty, Doctor, Date, Services
from rest_framework import serializers
from account.serializers import UserSerializer


class SpecialtySerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialty
        fields = (
            'name',
        )


class DoctorSerializer(serializers.ModelSerializer):
    specialty = SpecialtySerializer(many=True, read_only=True)
    class Meta:
        model = Doctor
        fields = (
            'id',
            'specialty',
            'image',
            'name',
            'description'    
        )


class ReserveSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only= True)
    created_at = serializers.DateTimeField(format="%Y-%m-%d")
    specialty = SpecialtySerializer(many=True, read_only=True)
    doctor = DoctorSerializer(many=True, read_only=True)
    
    class Meta:
        model = Reserve
        fields = (
            'id',
            'body',
            'created_at',
            'reserve_date',
            'created_by',
            'attachment',
            'specialty',
            'email',
            'phone',
            'doctor',
    )
        
class DateSerializer(serializers.ModelSerializer):
    date_at = serializers.DateTimeField(format="%Y-%m-%d")
    doctor = serializers.StringRelatedField(read_only= True, many=True)

    class Meta:
        model = Date
        fields = (
            'name',
            'email',
            'slug',
            'phone',
            'date_at',
            'doctor'
    )

class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = (
            'id',
            'title',
            'slug',
            'description',
            'get_thumbnails',
        )

class ServicesDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = (
            'id',
            'title',
            'slug',
            'description',
            'get_thumbnails',
        )


class SpecialtySerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialty
        fields = (
            'name',
        )


class DoctorSerializer(serializers.ModelSerializer):
    specialty = serializers.StringRelatedField(read_only= True, many=True)
    class Meta:
        model = Doctor
        fields = (
            'specialty',
            'get_thumbnails',
            'name',
            'description',
        )

