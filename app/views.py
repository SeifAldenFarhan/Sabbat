from django.apps import apps
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from paypal.standard.forms import PayPalPaymentsForm

from Sabat import settings
from app.forms import ContactForm, DonationForm
from app.models import AboutUs, Donation, City, Gallery, Training, DonationInfo


# Create your views here.

def index(request):
    return render(request, 'index.html')


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
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'success.html')
    form = ContactForm()
    context = {'form': form}
    return render(request, 'contact_us.html', context)


def city(request, city):
    city = City.objects.get(name=city)
    return render(request, 'city.html', {'city': city})


def village(request, city, village):
    return render(request, 'village.html')


def gallery_blog(request, id):
    blog = Gallery.objects.get(id=id)
    return render(request, 'blog.html', {'blog': blog})


def training_blog(request, id):
    blog = Training.objects.get(id=id)
    return render(request, 'blog.html', {'blog': blog})


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
    return render(request, 'donation.html', {'donation_info': donation_info, "DonationForm": DonationForm})


@csrf_exempt
def payment_done(request):
    return render(request, 'payment_done.html')


@csrf_exempt
def payment_canceled(request):
    return render(request, 'payment_cancelled.html')


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
    return render(request, 'process_payment.html', {'form': form})
