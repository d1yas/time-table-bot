from rest_framework import serializers
from .models import *


class UserSRL(serializers.ModelSerializer):
    class Meta:
        model = TeacherModel
        fields = "__all__"


class Login_Serializer(serializers.ModelSerializer):
    class Meta:
        model = StudentModel
        fields = "__all__"



