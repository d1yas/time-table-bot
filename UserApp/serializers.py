from rest_framework import serializers
from .models import StudentsTable, TeacherTableModel, CallTimesModel


class TeacherSrl(serializers.ModelSerializer):
    class Meta:
        model = TeacherTableModel
        fields = "__all__"


class StudentSrl(serializers.ModelSerializer):
    class Meta:
        model = StudentsTable
        fields = "__all__"


class CallTimesSrl(serializers.ModelSerializer):
    model = CallTimesModel
    fields = "__all__"
