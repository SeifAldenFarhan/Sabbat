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
    return render(request, 'index.html', {"cities": cities, 'current_path': 'en' + request.get_full_path()})


def about_us(request):
    about_us = AboutUs.objects.get(id=1)
    return render(request, 'about_us.html',
                  {'text': about_us.text, 'current_path': 'en' + str(request.get_full_path())})


def visiting_times(request):
    return render(request, 'visiting_times.html', {'current_path': 'en' + str(request.get_full_path())})


def membership(request):
    return render(request, 'membership.html', {'current_path': 'en' + str(request.get_full_path())})


def market(request):
    return render(request, 'market.html', {'current_path': 'en' + str(request.get_full_path())})


def market_type(request, type):
    market_list = ["Embroidery", "Accessories", "Book", "Herb", "Olive"]
    if type in market_list:
        Model = apps.get_model('app', type)
        objects = Model.objects.all()
        print(objects)
        return render(request, 'market_type.html', {'title': type, 'objects': objects})
    return render(request, 'market.html', {'current_path': 'en' + str(request.get_full_path())})


def gallery(request):
    objs = Gallery.objects.all()
    return render(request, 'gallery.html', {'gallery': objs, 'current_path': 'en' + str(request.get_full_path())})


def oral_history(request):
    return render(request, 'oral_history.html', {'current_path': 'en' + str(request.get_full_path())})


def training(request):
    objs = Training.objects.all()
    return render(request, 'training.html', {'training': objs, 'current_path': 'en' + str(request.get_full_path())})


def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'success.html')
    form = ContactForm()
    context = {'form': form, 'current_path': 'en' + str(request.get_full_path())}
    return render(request, 'contact_us.html', context)


def city(request, city):
    city = City.objects.get(name_en=city)
    print(request.get_full_path())
    return render(request, 'city.html', {'city': city, 'current_path': 'en' + str(request.get_full_path())})


def village(request, city, village):
    village = Village.objects.get(city__name_en=city, name_en=village)
    new_url = 'en' + request.get_full_path()
    return render(request, 'village.html', {'village': village, 'current_path': new_url})


def gallery_blog(request, id):
    blog = Gallery.objects.get(id=id)
    return render(request, 'blog.html', {'blog': blog, 'current_path': 'en' + str(request.get_full_path())})


def training_blog(request, id):
    blog = Training.objects.get(id=id)
    return render(request, 'blog.html', {'blog': blog, 'current_path': 'en' + str(request.get_full_path())})


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
    return render(request, 'donation.html', {'donation_info': donation_info, "DonationForm": DonationForm,
                                             'current_path': 'en' + str(request.get_full_path())})


@csrf_exempt
def payment_done(request):
    return render(request, 'payment_done.html', {'current_path': 'en' + str(request.get_full_path())})


@csrf_exempt
def payment_canceled(request):
    return render(request, 'payment_cancelled.html', {'current_path': 'en' + str(request.get_full_path())})


def checkout(request):
    if request.method == 'POST':
        return redirect('process_payment', {'current_path': 'en' + str(request.get_full_path())})


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
    return render(request, 'process_payment.html', {'form': form, 'current_path': 'en' + str(request.get_full_path())})


def museum(request):
    objs = MuseumPhoto.objects.all()
    return render(request, 'museum.html', {'photos': objs, 'current_path': 'en' + str(request.get_full_path())})
