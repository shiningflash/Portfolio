# Generated by Django 3.1.4 on 2021-01-09 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume_app', '0007_auto_20210109_1211'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(default='', max_length=1000)),
                ('institute1', models.CharField(default='', max_length=1000)),
                ('result1', models.CharField(default='', max_length=1000)),
                ('description1', models.CharField(default='', max_length=1000)),
                ('institute2', models.CharField(default='', max_length=1000)),
                ('result2', models.CharField(default='', max_length=1000)),
                ('description2', models.CharField(default='', max_length=1000)),
                ('institute3', models.CharField(default='', max_length=1000)),
                ('result3', models.CharField(default='', max_length=1000)),
                ('description3', models.CharField(default='', max_length=1000)),
            ],
        ),
    ]