# Generated by Django 4.1.5 on 2023-03-07 06:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_rename_pincode_student_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='Phone',
            new_name='phone',
        ),
    ]