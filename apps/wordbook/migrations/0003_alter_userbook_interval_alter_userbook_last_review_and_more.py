# Generated by Django 4.0.4 on 2022-04-26 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wordbook', '0002_remove_userbook_nivel_userbook_easiness_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbook',
            name='interval',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userbook',
            name='last_review',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userbook',
            name='repetitions',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
