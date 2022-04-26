# Generated by Django 4.0.4 on 2022-04-26 14:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wordbook', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userbook',
            name='nivel',
        ),
        migrations.AddField(
            model_name='userbook',
            name='easiness',
            field=models.PositiveIntegerField(default=5, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='userbook',
            name='interval',
            field=models.IntegerField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='userbook',
            name='last_review',
            field=models.DateField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='userbook',
            name='repetitions',
            field=models.IntegerField(blank=True, max_length=254, null=True),
        ),
    ]
