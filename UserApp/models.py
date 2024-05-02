from django.db import models
import os


class TeacherTableModel(models.Model):
    FIO_Teacher = models.CharField(max_length=225, unique=True)
    photo = models.ImageField(upload_to="uploads/teacher/", null=True)

    def __str__(self):
        return self.FIO_Teacher


class StudentsTable(models.Model):
    class_number = models.IntegerField()
    type_choise = (
        ("А", "A"),
        ("Б", "Б"),
        ("В", "В"),
        ("Г", "Г"),
        ("Д", "Д"),
        ("Е", "Е"),
    )
    class_type = models.CharField(choices=type_choise, max_length=225)
    table_photo = models.ImageField(upload_to="uploads/students/")

    def __str__(self):
        return "{} {}".format(self.class_number, self.class_type)


class CallTimesModel(models.Model):
    CHOICES = (
        ("Понедельник, Вторник, Среда, Суббота", "Понедельник, Вторник, Среда, Суббота"),
        ("Четверг", "Четверг"),
        ("Пятница", "Пятница")
    )
    hafta_kuni = models.CharField(choices=CHOICES, max_length=225, unique=True)
    time_photo = models.ImageField(upload_to="uploads/calltimes/")

    def __str__(self):
        return self.hafta_kuni
