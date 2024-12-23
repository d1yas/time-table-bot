# Generated by Django 4.2.8 on 2024-05-04 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CallTimesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hafta_kuni', models.CharField(choices=[('Понедельник, Вторник, Среда, Суббота', 'Понедельник, Вторник, Среда, Суббота'), ('Четверг', 'Четверг'), ('Пятница', 'Пятница')], max_length=225, unique=True)),
                ('time_photo', models.ImageField(upload_to='uploads/calltimes/')),
            ],
        ),
        migrations.CreateModel(
            name='StudentsTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_number', models.IntegerField()),
                ('class_type', models.CharField(choices=[('А', 'A'), ('Б', 'Б'), ('В', 'В'), ('Г', 'Г'), ('Д', 'Д'), ('Е', 'Е')], max_length=225)),
                ('table_photo', models.ImageField(upload_to='uploads/students/')),
            ],
        ),
        migrations.CreateModel(
            name='TeacherTableModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FIO_Teacher', models.CharField(max_length=225, unique=True)),
                ('photo', models.ImageField(null=True, upload_to='uploads/teacher/')),
            ],
        ),
    ]
