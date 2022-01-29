from django.shortcuts import render

from app.models import AboutUs


# Create your views here.

def index(request):
    return render(request, 'index.html')


def donation(request):
    return render(request, 'donation.html')


def about_us(request):
    about_us = AboutUs.objects.get(id=1)
    return render(request, 'about_us.html', {'text': about_us.text})


def visiting_times(request):
    return render(request, 'visiting_times.html')


def membership(request):
    return render(request, 'membership.html')
