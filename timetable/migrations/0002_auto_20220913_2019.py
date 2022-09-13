# Generated by Django 3.1.4 on 2022-09-13 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='department_name',
            field=models.CharField(max_length=100, unique=True, verbose_name='Department'),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='faculty_name',
            field=models.CharField(max_length=100, unique=True, verbose_name='Faculty'),
        ),
        migrations.AlterField(
            model_name='programme',
            name='programme_name',
            field=models.CharField(help_text='Ex: Information Technology (BSc) Level 100', max_length=100, unique=True, verbose_name='Programme'),
        ),
        migrations.AlterField(
            model_name='venue',
            name='room',
            field=models.CharField(max_length=100, unique=True, verbose_name='Venue Name'),
        ),
    ]