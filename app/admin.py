from django.contrib import admin

from app.models import City, Village, ImageCity, ImageVillage, AboutUs, Donation

# Register your models here.

admin.site.register(AboutUs)
admin.site.register(City)
admin.site.register(Village)
admin.site.register(ImageCity)
admin.site.register(ImageVillage)
admin.site.register(Donation)
