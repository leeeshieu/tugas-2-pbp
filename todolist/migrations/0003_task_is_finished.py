# Generated by Django 4.1 on 2022-09-27 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0002_alter_task_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='is_finished',
            field=models.BooleanField(default=False, verbose_name=False),
            preserve_default=False,
        ),
    ]
