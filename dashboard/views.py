from django.shortcuts import render
from django.http import HttpResponse
from .models import Customer

# Create your views here.
def index(request):
    # summary in this view
    # latest customers
    recent_customers = Customer.objects.all()[:5]
    # latest payments
    # latest tasks
    # etc.
    return HttpResponse('Dashbord gonna be here later')

def customer(request):
    # get customers list
    customers = Customer.objects.all()
    # create a string from it and return
    return render(request, 'customers.html', {
        'customer_list': customers,
    })
    #return HttpResponse('Customers view will be here later')

def customer_details(request, cid):
    customer = Customer.objects.get(id=cid)

    return HttpResponse(f'Displaying details of customer: {cid} -> {customer.first_name} {customer.last_name}')


