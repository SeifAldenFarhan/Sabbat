from django.urls import path

from app import views

app_name = 'app'

urlpatterns = [
    path('', views.index, name='index'),
    path('donation', views.donation, name='donation'),
    path('aboutus', views.about_us, name='about_us'),
    path('visitingtimes', views.visiting_times, name='visiting_times'),
    path('membership', views.membership, name='membership'),
    path('market', views.market, name='market'),
    path('market/<str:title>', views.market_type, name='market_type'),

    path('gallery', views.gallery, name='gallery'),
    path('oralhistory', views.oral_history, name='oral_history'),
    path('training', views.training, name='training'),
    path('contactus', views.contact_us, name='contact_us'),




]
