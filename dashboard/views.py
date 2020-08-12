from django.shortcuts import render
from django.http import HttpResponse
from .models import Customer, Payment, Task

# Create your views here.
def index(request):
    # summary in this view
    # latest customers
    recent_customers = Customer.objects.order_by('-created')[0:5]
    # latest payments
    recent_payments = Payment.objects.filter(status=1).order_by('-created')[0:5]
    payments_number = len(recent_payments)

    income = sum(payment.amount for payment in recent_payments)
    print(income)
    
    #income = sum(recent_payments.amount)
    # latest tasks
    recent_tasks = Task.objects.order_by('-created')[0:5]
    # etc.
    return render(request, 
        'dashboard.html', 
        {
            'customer_list':recent_customers,
            'payments_list':recent_payments,
            'payments_number': payments_number,
            'income': income,
            'tasks_list':recent_tasks,
        })


def customer(request):
    # get customers list
    customers = Customer.objects.order_by('-created')
    # create a string from it and return
    return render(request, 'customers.html', {
        'customer_list': customers,
    })
    #return HttpResponse('Customers view will be here later')

def customer_details(request, cid):
    customer = Customer.objects.get(id=cid)

    return render(request, 
        'customer_detail.html',
        {
            'cst': customer
        }
    
    )
    #return HttpResponse(f'Displaying details of customer: {cid} -> {customer.first_name} {customer.last_name}')

def payment_list(request):
    payments = Payment.objects.order_by('-created')

    return render(
        request,
        'payment_list.html',
        {
            'payments_list': payments
        }
    )

def payment_details(request, pid):
    payment = Payment.objects.get(id=pid)

    return HttpResponse(f'Payment id: {payment.id} details will be here')

def task_detail(srequest, pid):
    payment = Payment.objects.get(id=pid)

    return HttpResponse(f'Payment id: {payment.id} details will be here')