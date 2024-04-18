from django.db import models
class AddTimeTable(models.Model):
    tametable = models.ImageField(upload_to='uploads/')

class TeacherModel(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    patronymic = models.CharField(max_length=20)
class StudentModel(models.Model):
    class_name = models.CharField(max_length=5)



    def __str__(self):
        return self.name