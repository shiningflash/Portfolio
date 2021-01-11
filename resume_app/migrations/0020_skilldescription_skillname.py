# Generated by Django 3.1.4 on 2021-01-09 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume_app', '0019_auto_20210109_1632'),
    ]

    operations = [
        migrations.CreateModel(
            name='SkillDescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_description', models.CharField(default='', max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='SkillName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(default='', max_length=1000)),
                ('skill_percentage', models.CharField(default='', max_length=100)),
            ],
        ),
    ]