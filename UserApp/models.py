from django.db import models
import os
class TeacherModel(models.Model):
    surname = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    patronymic = models.CharField(max_length=20)
    table = models.ImageField(upload_to="uploads/teacher/")

    def __str__(self):
        return f"{self.surname} {self.name} {self.patronymic}"





def get_upload_path(instance, filename):
    # Определяем путь к папке в зависимости от выбранного класса
    class_folder = instance.class_name.replace(" ", "_").lower()
    # Составляем путь для сохранения изображения
    upload_path = os.path.join("uploads", "students", class_folder, filename)
    return upload_path


class StudentModel(models.Model):
    CHOICES = (
        ("1 А", "1 А"),
        ("1 Б", "1 Б"),
        ("1 В", "1 В"),
        ("1 Г", "1 Г"),
        ("1 Д", "1 Д"),
        ("1 Е", "1 Е"),
        ("2 А", "2 А"),
        ("2 Б", "2 Б"),
        ("2 В", "2 В"),
        ("2 Г", "2 Г"),
        ("2 Д", "2 Д"),
        ("2 Е", "2 Е"),
        ("3 А", "3 А"),
        ("3 Б", "3 Б"),
        ("3 В", "3 В"),
        ("3 Г", "3 Г"),
        ("3 Д", "3 Д"),
        ("3 Е", "3 Е"),
        ("4 А", "4 А"),
        ("4 Б", "4 Б"),
        ("4 В", "4 В"),
        ("4 Г", "4 Г"),
        ("4 Д", "4 Д"),
        ("4 Е", "4 Е"),
        ("5 А", "5 А"),
        ("5 Б", "5 Б"),
        ("5 В", "5 В"),
        ("5 Г", "5 Г"),
        ("5 Д", "5 Д"),
        ("5 Е", "5 Е"),
        ("6 А", "6 А"),
        ("6 Б", "6 Б"),
        ("6 В", "6 В"),
        ("6 Г", "6 Г"),
        ("6 Д", "6 Д"),
        ("6 Е", "6 Е"),
        ("7 А", "7 А"),
        ("7 Б", "7 Б"),
        ("7 В", "7 В"),
        ("7 Г", "7 Г"),
        ("7 Д", "7 Д"),
        ("7 Е", "7 Е"),
        ("8 А", "8 А"),
        ("8 Б", "8 Б"),
        ("8 В", "8 В"),
        ("8 Г", "8 Г"),
        ("8 Д", "8 Д"),
        ("8 Е", "8 Е"),
        ("9 А", "9 А"),
        ("9 Б", "9 Б"),
        ("9 В", "9 В"),
        ("9 Г", "9 Г"),
        ("9 Д", "9 Д"),
        ("9 Е", "9 Е"),
        ("10 А", "10 А"),
        ("10 Б", "10 Б"),
        ("10 В", "10 В"),
        ("10 Г", "10 Г"),
        ("10 Д", "10 Д"),
        ("10 Е", "10 Е"),
        ("11 А", "11 А"),
        ("11 Б", "11 Б"),
        ("11 В", "11 В"),
        ("11 Г", "11 Г"),
        ("11 Д", "11 Д"),
        ("11 Е", "11 Е"),
    )

    class_name = models.CharField(choices=CHOICES, max_length=225)
    time_table_students = models.ImageField(upload_to=get_upload_path)
    add_table = models.ImageField(upload_to=get_upload_path)

    def __str__(self):
        return self.class_name



