from django.urls import path
from . import views


urlpatterns = [
    path('cart/<int:index>/', views.cart, name = 'cart'),
    path('cart/week/<int:index>/', views.cart_week, name = 'cart_week'),
    path('cart/mounth/<int:index>/', views.cart_mounth, name = 'cart_mounth'),
    path('cart/year/<int:index>/', views.cart_year, name = 'cart_year'),
    path('product/create/', views.create_product, name = 'create_product'),
]