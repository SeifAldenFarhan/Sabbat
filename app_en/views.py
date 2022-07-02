from django.apps import apps
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from paypal.standard.forms import PayPalPaymentsForm

from Sabat import settings
from app.forms import ContactForm, DonationForm
from app.models import AboutUs, Donation, City, Gallery, Training, DonationInfo, MuseumPhoto, Village


# Create your views here.

def index(request):
    cities = City.objects.all()
    print(cities)
    cities[0].name = "12345"
    cities[0].save()
    print(cities[0].name)

    return render(request, 'index_en.html', {"cities": cities})


def about_us(request):
    about_us = AboutUs.objects.get(id=1)
    text = about_us.text_en.split('\n')
    return render(request, 'about_us_en.html', {'text': text})


def visiting_times(request):
    return render(request, 'visiting_times_en.html')


def membership(request):
    return render(request, 'membership_en.html')


def market(request):
    return render(request, 'market_en.html')


def market_type(request, type):
    market_list = ["Embroidery", "Accessories", "Book", "Herb", "Olive"]
    if type in market_list:
        Model = apps.get_model('app', type)
        objects = Model.objects.all()
        print(objects)
        return render(request, 'market_type_en.html', {'title': type, 'objects': objects})
    return render(request, 'market_en.html')


def gallery(request):
    objs = Gallery.objects.all()
    return render(request, 'gallery_en.html', {'gallery': objs})


def oral_history(request):
    return render(request, 'oral_history_en.html')


def training(request):
    objs = Training.objects.all()
    return render(request, 'training_en.html', {'training': objs})


def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'success_en.html')
    form = ContactForm()
    context = {'form': form}
    return render(request, 'contact_us_en.html', context)


def city(request, city):
    city = City.objects.get(name_en=city)
    return render(request, 'city_en.html', {'city': city})


def village(request, city, village):
    village = Village.objects.get(city__name_en=city, name_en=village)
    return render(request, 'village_en.html', {'village': village})


def gallery_blog(request, id):
    blog = Gallery.objects.get(id=id)
    return render(request, 'blog_en.html', {'blog': blog})


def training_blog(request, id):
    blog = Training.objects.get(id=id)
    return render(request, 'blog_en.html', {'blog': blog})


def donation(request):
    donation_info = Donation.objects.get(id=1)
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            form.save()
            amount = form['amount']
            d_id = DonationInfo.objects.latest('d_id')

            print(amount, d_id)
            return HttpResponseRedirect(reverse(f'app:process_payment', args=[amount, d_id]))

            # process_payment(request, amount, d_id)
    return render(request, 'donation_en.html', {'donation_info': donation_info, "DonationForm": DonationForm})


@csrf_exempt
def payment_done(request):
    return render(request, 'payment_done_en.html')


@csrf_exempt
def payment_canceled(request):
    return render(request, 'payment_cancelled_en.html')


def checkout(request):
    if request.method == 'POST':
        return redirect('process_payment')


def process_payment(request, amount, d_id):
    host = request.get_host()
    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': amount,
        'item_name': 'Donation - amount: {}'.format(amount),
        'invoice': str(d_id),
        'currency_code': 'ILS',
        'notify_url': 'http://{}{}'.format(host, reverse('paypal-ipn')),
        'return_url': 'http://{}/{}'.format(host, reverse('app:payment_done')),
        'cancel_return': 'http://{}{}'.format(host, reverse('app:payment_cancelled')),
    }
    form = PayPalPaymentsForm(initial=paypal_dict)
    return render(request, 'process_payment_en.html', {'form': form})


def museum(request):
    objs = MuseumPhoto.objects.all()
    return render(request, 'museum_en.html', {'photos': objs})
