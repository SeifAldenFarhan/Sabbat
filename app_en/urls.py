from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from Sabat import settings
from app_en import views

app_name = 'app_en'

urlpatterns = [
    path('', views.index, name='index_en'),
    path('city/<str:city>', views.city, name='city_en'),
    path('city/<str:city>/<str:village>', views.village, name='village_en'),

    path('donation', views.donation, name='donation_en'),
    path('aboutus', views.about_us, name='about_us_en'),
    path('visitingtimes', views.visiting_times, name='visiting_times_en'),
    path('membership', views.membership, name='membership_en'),
    path('museum', views.museum, name='museum_en'),
    path('market', views.market, name='market_en'),
    path('market/<str:type>', views.market_type, name='market_type_en'),
    path('gallery', views.gallery, name='gallery_en'),
    path('gallery/<int:id>', views.gallery_blog, name='gallery_blog_en'),
    path('oralhistory', views.oral_history, name='oral_history_en'),
    path('training', views.training, name='training_en'),
    path('training/<int:id>', views.training_blog, name='training_blog_en'),
    path('contactus', views.contact_us, name='contact_us_en'),
    path('processpayment/<str:d_id>/<str:amount>', views.process_payment, name='process_payment_en'),
    path('payment-done', views.payment_done, name='payment_done_en'),
    path('payment-cancelled', views.payment_canceled, name='payment_cancelled_en'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_DIR)
