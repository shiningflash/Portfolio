from django.shortcuts import render
from .models import Resume, Form, Field, Education, Experience, Review, \
    Portfolio, SkillName, SkillDescription, Awards, Certificate, MetaData

def home(request):
    resume = Resume.objects.get(pk=1)
    field = Field.objects.get(pk=1)
    education = Education.objects.get(pk=1)
    experience = Experience.objects.get(pk=1)
    review = Review.objects.get(pk=1)
    portfolio = Portfolio.objects.all()
    skill_description = SkillDescription.objects.all()
    skill = SkillName.objects.all()
    awards = Awards.objects.all()
    certificate = Certificate.objects.all()
    metadata = MetaData.objects.get(pk=1)

    context = {
            "resume": resume,
            "field": field,
            "education": education,
            "experience": experience,
            "review": review,
            "portfolio": portfolio,
            "skill_description": skill_description,
            "skill": skill,
            "awards": awards,
            "certificate": certificate,
            "metadata": metadata
        }
    return render(request, 'resume/home.html', context)

def contact(request):
    resume = Resume.objects.get(pk=1)
    field = Field.objects.get(pk=1)
    education = Education.objects.get(pk=1)
    experience = Experience.objects.get(pk=1)
    review = Review.objects.get(pk=1)
    portfolio = Portfolio.objects.all()
    skill_description = SkillDescription.objects.all()
    skill = SkillName.objects.all()
    awards = Awards.objects.all()
    certificate = Certificate.objects.all()
    metadata = MetaData.objects.get(pk=1)

    if request.method == 'POST':
        contact_name = request.POST['contact_name']
        contact_email = request.POST['contact_email']
        contact_message = request.POST['contact_message']

        form = Form(
            contact_name=contact_name,
            contact_email=contact_email,
            contact_message=contact_message
        )
        context = {
            "resume": resume,
            "form": form,
            "field": field,
            "education": education,
            "experience": experience,
            "review": review,
            "portfolio": portfolio,
            "skill_description": skill_description,
            "skill": skill,
            "awards": awards,
            "certificate": certificate,
            "metadata": metadata
        }
        if len(contact_name) > 2:
            form.save()

    if request.method == 'GET':
        context = {
            "resume": resume,
            "field": field,
            "education": education,
            "experience": experience,
            "review": review,
            "portfolio": portfolio,
            "skill_description": skill_description,
            "skill": skill,
            "awards": awards,
            "certificate": certificate,
            "metadata": metadata
        }

    return render(request, 'resume/home.html', context)