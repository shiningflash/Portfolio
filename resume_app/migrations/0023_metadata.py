# Generated by Django 3.1.4 on 2021-01-12 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume_app', '0022_auto_20210110_0521'),
    ]

    operations = [
        migrations.CreateModel(
            name='MetaData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meta_img', models.ImageField(default='resume_app/static/images/portf.png', upload_to='meta_img/%y')),
                ('meta_type', models.CharField(default='website', max_length=1000)),
            ],
        ),
    ]
