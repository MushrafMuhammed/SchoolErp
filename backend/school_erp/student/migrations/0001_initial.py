# Generated by Django 4.1.5 on 2023-01-27 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(max_length=25)),
                ('name', models.CharField(max_length=25)),
                ('dob', models.CharField(max_length=25)),
                ('guardian_name', models.CharField(max_length=25)),
                ('gender', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=40)),
                ('place', models.CharField(max_length=30)),
                ('pincode', models.CharField(max_length=6)),
                ('email', models.EmailField(max_length=50)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]