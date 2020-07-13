

from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name="HOME"),
    path('about/', views.about, name="About"),
    path('contact/', views.contact, name="Contact"),
    path('product/', views.product, name="Product"),
    path('search/', views.search, name="Srarch"),
    path('checkout/', views.checkout, name="Checkout"),
    path('tracker/', views.tracker, name="Tracker"),


]
