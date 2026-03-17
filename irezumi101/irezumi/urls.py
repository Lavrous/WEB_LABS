# irezumi/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('tattoos/<slug:tattoo_slug>/', views.tattoo_detail, name='tattoo'),
]