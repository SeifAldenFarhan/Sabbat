from django.urls import re_path

from app import views

app_name = 'app'

urlpatterns = [
    re_path('', views.index, name='index')
]
