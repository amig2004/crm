from django.db import models

# Create your models here.
class Customer(models.Model):
    MARKETS = [
        ('PL', 'Poland'),
        ('DE', 'Germany'),
        ('UA', 'Ukraine'),
        ('FR', 'France')
    ]

    RISK_LEVELS = [
            ('L', 'Low'),
            ('M', 'Medium'),
            ('H', 'High'),
        ]

    # logging data
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    # customer data
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    market = models.CharField(max_length=2, choices=MARKETS)
    account_number= models.CharField(max_length=26) 
    risk_level = models.CharField(max_length=1, choices=RISK_LEVELS)
    offer_consent = models.BooleanField()
    automatic_consent = models.BooleanField()

    # 
    active = models.BooleanField(default=True)


    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Payment(models.Model):

    class PaymentStatus(models.IntegerChoices):
        NotAccepted = 0
        Accepted = 1
        Removed = 2

    # logging data
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    # data
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    amount = models.DecimalField(decimal_places=2, max_digits=9)
    title = models.CharField(max_length=300)
    status = models.IntegerField(choices=PaymentStatus.choices)

    def __str__(self):
        return f'{self.title} / {self.amount} / {self.user}'



class Task(models.Model):

    class TaskStatus(models.IntegerChoices):
        Prepared = 0
        Scheduled = 1
        Initiated = 2
        Pending = 3
        Done = 4 

    # logging data
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    # task data
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    status = models.IntegerField(default=0, choices=TaskStatus.choices)
    json = models.TextField()
    annotations = models.CharField(max_length=250)

    def __str__(self):
        return f'{self.user} -> {self.name}'




