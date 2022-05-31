from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.urls import path, include

from Sabat import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('app.urls', 'app'), namespace='app')),
    path('en/', include(('app_en.urls', 'app_en'), namespace='app_en')),
    path('paypal/', include('paypal.standard.ipn.urls')),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_DIR)
