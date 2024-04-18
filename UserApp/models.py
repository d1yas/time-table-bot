from django.db import models
class AddTable(models.Model):
    timetable = models.ImageField(upload_to='uploads/')
    class_name_table = models.CharField(max_length=2, unique=True)
    def __str__(self):
        return self.class_name_table

class TeacherModel(models.Model):
    surname = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    patronymic = models.CharField(max_length=20)
    def __str__(self):
        return f"{self.surname} {self.name} {self.patronymic}"

class StudentModel(models.Model):
    class_name = models.CharField(max_length=5, unique=True)
    def __str__(self):
        return self.class_name



