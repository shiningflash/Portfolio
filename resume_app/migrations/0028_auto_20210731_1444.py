# Generated by Django 3.1.4 on 2021-07-31 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume_app', '0027_auto_20210731_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userip',
            name='ip',
            field=models.CharField(default=None, max_length=100, unique=True),
        ),
    ]