from django.db import models

import uuid
import os

def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('resume_app/static/images/', 'profile.jpg')

class Resume(models.Model):
    name = models.CharField(max_length=50, default='Amirul Islam')
    first_name = models.CharField(max_length=50, default='Amirul')
    full_name = models.CharField(max_length=100, default='Amirul Islam Al Mamun')
    title = models.CharField(max_length=100, default='')

    resume_download_url = models.CharField(max_length=1000, default='')
    resume_note = models.CharField(max_length=1000, default='')

    description1 = models.CharField(max_length=1000, default='')
    description2 = models.CharField(max_length=1000, default='')
    description3 = models.CharField(max_length=1000, default='')

    # image = models.ImageField(upload_to='resume_app/static/images/', default='resume_app/static/images/profile.jpg')
    image = models.FileField(upload_to=get_file_path,
                        null=True,
                        blank=True,
                        default='resume_app/static/images/profile.jpg')

    portfolio_description = models.CharField(max_length=1000, default='')

    awards_description = models.CharField(max_length=1000, default='')
    certificate_description = models.CharField(max_length=1000, default='')

    bio = models.CharField(max_length=100)
    address = models.CharField(max_length=1000)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    github = models.CharField(max_length=100, default='')
    twitter = models.CharField(max_length=100, default='')
    facebook = models.CharField(max_length=100, default='')
    linkedin = models.CharField(max_length=100, default='')


class Form(models.Model):
    contact_name = models.CharField(max_length=50)
    contact_email = models.CharField(max_length=50)
    contact_message = models.CharField(max_length=1000)

    def __str__(self):
        return self.contact_name

class Field(models.Model):
    wf_name1 = models.CharField(max_length=100, default='')
    wf_description1 = models.CharField(max_length=1000, default='')
    wf_name2 = models.CharField(max_length=100, default='')
    wf_description2 = models.CharField(max_length=1000, default='')

class Education(models.Model):
    description = models.CharField(max_length=1000, default='')
    degree1 = models.CharField(max_length=1000, default='')
    institute1 = models.CharField(max_length=1000, default='')
    result1 = models.CharField(max_length=1000, default='')
    description1 = models.CharField(max_length=1000, default='')
    degree2 = models.CharField(max_length=1000, default='')
    institute2 = models.CharField(max_length=1000, default='')
    result2 = models.CharField(max_length=1000, default='')
    description2 = models.CharField(max_length=1000, default='')
    degree3 = models.CharField(max_length=1000, default='')
    institute3 = models.CharField(max_length=1000, default='')
    result3 = models.CharField(max_length=1000, default='')
    description3 = models.CharField(max_length=1000, default='')

class Experience(models.Model):
    description = models.CharField(max_length=1000, default='')
    position1 = models.CharField(max_length=1000, default='')
    company1 = models.CharField(max_length=1000, default='')
    duration1 = models.CharField(max_length=1000, default='')
    description11 = models.CharField(max_length=1000, default='')
    description12 = models.CharField(max_length=1000, default='')
    position2 = models.CharField(max_length=1000, default='')
    company2 = models.CharField(max_length=1000, default='')
    duration2 = models.CharField(max_length=1000, default='')
    description21 = models.CharField(max_length=1000, default='')
    description22 = models.CharField(max_length=1000, default='')
    position3 = models.CharField(max_length=1000, default='')
    company3 = models.CharField(max_length=1000, default='')
    duration3 = models.CharField(max_length=1000, default='')
    description31 = models.CharField(max_length=1000, default='')
    description32 = models.CharField(max_length=1000, default='')

class Review(models.Model):
    review1 = models.CharField(max_length=1000, default='')
    reviewer1 = models.CharField(max_length=1000, default='')
    review2 = models.CharField(max_length=1000, default='')
    reviewer2 = models.CharField(max_length=1000, default='')
    review3 = models.CharField(max_length=1000, default='')
    reviewer3 = models.CharField(max_length=1000, default='')

class Portfolio(models.Model):
    project_name = models.CharField(max_length=1000, default='')
    project_image = models.ImageField(upload_to="portfolio/%y")
    project_url = models.CharField(max_length=1000, default='#')

    def __str__(self):
        return self.project_name

class SkillDescription(models.Model):
    skill_description = models.CharField(max_length=2000, default='')

class SkillName(models.Model):
    skill_name = models.CharField(max_length=1000, default='')
    skill_percentage = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.skill_name

class Awards(models.Model):
    title = models.CharField(max_length=1000, default='')
    description = models.CharField(max_length=1000, default='')

    def __str__(self):
        return self.title

class Certificate(models.Model):
    title = models.CharField(max_length=1000, default='')
    issued_by = models.CharField(max_length=1000, default='')
    certificate_url = models.CharField(max_length=1000, default='#')

    def __str__(self):
        return self.title

class MetaData(models.Model):
    meta_img = models.ImageField(upload_to="meta_img/%y", default='resume_app/static/images/portf.png')
    meta_type = models.CharField(max_length=1000, default='website')
    meta_title = models.CharField(max_length=1000, default='Amirul Islam')
    meta_des = models.CharField(max_length=1000, default='Follow me')

class UserIP(models.Model):
    ip = models.CharField(default=None, max_length=100, unique=True)
    first_visited = models.DateTimeField(auto_now_add=True)
    last_visited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.ip