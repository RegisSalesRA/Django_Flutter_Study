# Generated by Django 4.1.7 on 2023-03-23 23:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_remove_discipline_student_discipline_student'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='cpf',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='description',
        ),
    ]
