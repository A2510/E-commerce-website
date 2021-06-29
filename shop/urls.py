from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('home', views.index, name='home'),
    path('contact', views.contact, name='contact'),
    path('contact_handle', views.contact_handle, name='contact_handel'),
    path('item', views.Item, name='item')
]