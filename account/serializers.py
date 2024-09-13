from .models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    age =  serializers.DateTimeField(format="%Y-%m-%d")
    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'name',
            'get_avatar',
            'age',
            'slug',
            'is_active',
            'is_superuser',
            'is_staff',
            'is_doctor',
            'date_joined',
            'last_login'
]