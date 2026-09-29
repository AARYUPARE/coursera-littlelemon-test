from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('book/', views.book, name='book'),
    path('reservations/', views.reservations, name='reservations'),
    path('bookings', views.bookings_api, name='bookings_api'),
    path('bookings/', views.bookings_api, name='bookings_api_slash'),
]
