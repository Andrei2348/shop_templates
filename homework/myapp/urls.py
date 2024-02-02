from django.urls import path
from . import views


urlpatterns = [
    path('cart/<int:index>/', views.cart, name = 'cart'),
]