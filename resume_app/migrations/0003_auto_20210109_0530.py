# Generated by Django 3.1.4 on 2021-01-09 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume_app', '0002_auto_20210108_1838'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='description1',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='resume',
            name='description2',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='resume',
            name='description3',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='resume',
            name='first_name',
            field=models.CharField(default='Amirul', max_length=50),
        ),
        migrations.AddField(
            model_name='resume',
            name='full_name',
            field=models.CharField(default='Amirul Islam Al Mamun', max_length=100),
        ),
        migrations.AddField(
            model_name='resume',
            name='image',
            field=models.ImageField(default='resume_app/static/images/profile.jpg', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='resume',
            name='name',
            field=models.CharField(default='Amirul Islam', max_length=50),
        ),
        migrations.AddField(
            model_name='resume',
            name='title',
            field=models.CharField(default='', max_length=100),
        ),
    ]
