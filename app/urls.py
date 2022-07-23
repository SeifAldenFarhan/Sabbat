from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from Sabat import settings
from app import views

app_name = 'app'

urlpatterns = [
    path('', views.index, name='index'),
    path('city/<str:city>', views.city, name='city'),
    path('city/<str:city>/<str:village>', views.village, name='village'),

    path('donation', views.donation, name='donation'),
    path('aboutus', views.about_us, name='about_us'),
    path('visitingtimes', views.visiting_times, name='visiting_times'),
    path('membership', views.membership, name='membership'),
    path('museum', views.museum, name='museum'),
    path('market', views.market, name='market'),
    path('market/<str:type>', views.market_type, name='market_type'),
    path('gallery', views.gallery, name='gallery'),
    path('gallery/<int:id>', views.gallery_blog, name='gallery_blog'),
    path('oralhistory', views.oral_history, name='oral_history'),
    path('training', views.training, name='training'),
    path('training/<int:id>', views.training_blog, name='training_blog'),
    path('contactus', views.contact_us, name='contact_us'),
    path('processpayment/<str:d_id>/<str:amount>', views.process_payment, name='process_payment'),
    path('payment-done', views.payment_done, name='payment_done'),
    path('payment-cancelled', views.payment_canceled, name='payment_cancelled'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_DIR)
handler404 = 'app.views.handler404'
handler500 = 'app.views.handler500'