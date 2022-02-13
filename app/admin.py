from django.contrib import admin

from app.models import City, Village, ImageCity, ImageVillage, AboutUs, Donation, Embroidery, Accessories, Book, Herb, \
    Olive, OralHistory, Contact, Gallery, Training, DonationInfo

# Register your models here.

admin.site.register(AboutUs)
admin.site.register(City)
admin.site.register(Village)
admin.site.register(ImageCity)
admin.site.register(ImageVillage)
admin.site.register(Donation)
admin.site.register(OralHistory)
admin.site.register(Embroidery)
admin.site.register(Accessories)
admin.site.register(Book)
admin.site.register(Herb)
admin.site.register(Olive)
admin.site.register(Contact)
admin.site.register(Gallery)
admin.site.register(Training)
admin.site.register(DonationInfo)
