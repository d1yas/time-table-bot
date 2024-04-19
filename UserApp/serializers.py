from rest_framework import serializers
from .models import *


class TeacherSRL(serializers.ModelSerializer):
    class Meta:
        model = TeacherModel
        fields = "__all__"


class StudentSrl(serializers.ModelSerializer):
    class Meta:
        model = StudentModel
        fields = "__all__"



