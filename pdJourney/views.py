from django.shortcuts import render
from .models import LearningJourney, AboutMe

def index(request):
    journeys = LearningJourney.objects.all()
    return render(request, 'pdJourney/index.html', {'journeys': journeys})

def about_me(request):
    details = AboutMe.objects.all()
    return render(request, 'pdJourney/aboutMe.html', {'details': details})
