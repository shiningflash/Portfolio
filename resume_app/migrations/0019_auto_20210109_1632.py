# Generated by Django 3.1.4 on 2021-01-09 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume_app', '0018_portfolio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='project_image',
            field=models.ImageField(upload_to='portfolio/%y'),
        ),
    ]