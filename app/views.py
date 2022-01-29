from django.shortcuts import render

from app.models import AboutUs, Donation


# Create your views here.

def index(request):
    return render(request, 'index.html')


def donation(request):
    donation_info = Donation.objects.get(id=1)
    return render(request, 'donation.html', {'donation_info': donation_info})


def about_us(request):
    about_us = AboutUs.objects.get(id=1)
    return render(request, 'about_us.html', {'text': about_us.text})


def visiting_times(request):
    return render(request, 'visiting_times.html')


def membership(request):
    return render(request, 'membership.html')


def market(request):
    return render(request, 'market.html')


def gallery(request):
    return render(request, 'gallery.html')


def oral_history(request):
    return render(request, 'oral_history.html')


def training(request):
    return render(request, 'training.html')


def contact_us(request):
    return render(request, 'contact_us.html')
