from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('customer/', views.customer, name='customers'),
    path('customer/<int:cid>', views.customer_details, name='customer_details')
]