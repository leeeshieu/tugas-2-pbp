# Generated by Django 4.1 on 2022-09-28 02:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0003_task_is_finished'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='is_finished',
        ),
    ]