from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'index.html')


def donation(request):
    return render(request, 'donation.html')


def about_us(request):
    return render(request, 'about_us.html')


def visiting_times(request):
    return render(request, 'visiting_times.html')


def membership(request):
    return render(request, 'membership.html')