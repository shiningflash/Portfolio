# Generated by Django 3.1.4 on 2021-01-09 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume_app', '0012_resume_resume_download_link'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resume',
            old_name='resume_download_link',
            new_name='resume_download_url',
        ),
    ]
