from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Attendence

User = get_user_model()


class AttendenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendence
        fields = ['id', 'teacher', 'section',
                  'date', 'course_code', 'qr', 'student']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name", "email"]
