from django.forms import ModelForm

from .models import Contact, DonationInfo


class ContactForm(ModelForm):
    class Meta():
        model = Contact
        fields = '__all__'


class DonationForm(ModelForm):
    class Meta():
        model = DonationInfo
        fields = ('amount',)
