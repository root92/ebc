from django.shortcuts import render
from .models import Profil, MediaContent
# from django.contrib import h

# Create your views here.
def home(request):
    works_images = MediaContent.objects.all()
    enterprise = Profil.objects.all()
    context = {
        'works_images': works_images,
        'enterprise': enterprise
    }

    return render(request, 'home.html', context)


def about(request):
    return render(request, 'about.html')


def works(request):
    works_images = MediaContent.objects.all()
    enterprise = Profil.objects.all()
    context = {
        'works_images': works_images,
        'enterprise': enterprise
    }
    return render(request, 'realisation.html', context)


def contactus(request):
    return render(request, 'contactus.html')
    
