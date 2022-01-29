from django.urls import path

from app import views

app_name = 'app'

urlpatterns = [
    path('', views.index, name='index'),
    path('donation', views.donation, name='donation'),
    path('aboutus', views.about_us, name='about_us'),
    path('visitingtimes', views.visiting_times, name='visiting_times'),
    path('membership', views.membership, name='membership'),
]
