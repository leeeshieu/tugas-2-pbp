# Generated by Django 4.1 on 2022-09-28 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0004_remove_task_is_finished'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='is_finished',
            field=models.BooleanField(default=False, verbose_name=False),
            preserve_default=False,
        ),
    ]