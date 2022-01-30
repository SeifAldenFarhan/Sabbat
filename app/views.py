from django.shortcuts import render

from app.models import AboutUs, Donation
from django.apps import apps


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


def market_type(request, type):
    market_list = ["Embroidery", "Accessories", "Book", "Herb", "Olive"]
    if type in market_list:
        Model = apps.get_model('app', type)
        objects = Model.objects.all()
        print(objects)
        return render(request, 'market_type.html', {'title': type})
    return render(request, 'market.html')


def gallery(request):
    return render(request, 'gallery.html')


def oral_history(request):
    return render(request, 'oral_history.html')


def training(request):
    return render(request, 'training.html')


def contact_us(request):
    return render(request, 'contact_us.html')
