# Generated by Django 4.1.5 on 2023-01-27 06:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exams',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_name', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('remark', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=10)),
                ('dob', models.DateField()),
                ('pincode', models.CharField(max_length=25)),
                ('qualification', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=50)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]
