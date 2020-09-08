from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('laptops/', views.laptops, name='laptops'),
    path('add_laptop/', views.add_laptop, name = 'add_laptop'),
    path('update_laptop/<str:pk>', views.update_laptop, name = 'update_laptop'),
    path('delete/<str:pk>', views.delete, name = 'delete'),
]