# Generated by Django 3.1.4 on 2021-01-09 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume_app', '0008_education'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='degree1',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='education',
            name='degree2',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='education',
            name='degree3',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
