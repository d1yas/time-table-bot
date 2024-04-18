from django.shortcuts import render

from .models import TeacherModel
def filtr_by_TeacherModel(teachermodel_bot):
    teacher = TeacherModel.objects.all().filter(katalog=teachermodel_bot)
    return teacher
# Create your views here.
