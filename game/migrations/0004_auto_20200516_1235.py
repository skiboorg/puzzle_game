# Generated by Django 3.0.6 on 2020-05-16 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_remove_game_lev'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='end',
        ),
        migrations.RemoveField(
            model_name='game',
            name='time',
        ),
        migrations.AddField(
            model_name='game',
            name='result',
            field=models.BooleanField(default=False),
        ),
    ]
