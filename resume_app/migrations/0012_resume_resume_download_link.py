# Generated by Django 3.1.4 on 2021-01-09 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume_app', '0011_resume_resume_note'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='resume_download_link',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
