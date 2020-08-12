from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('customer/', views.customer, name='customers_list'),
    path('customer/<int:cid>', views.customer_details, name='customer_details'),
    path('payment', views.payment_list, name='payment_list'),
    path('payment/<int:pid>', views.payment_details, name='payment_details')
]