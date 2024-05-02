from django.contrib import admin
from .models import StudentsTable, TeacherTableModel, CallTimesModel

admin.site.register(StudentsTable)
admin.site.register(TeacherTableModel)
admin.site.register(CallTimesModel)