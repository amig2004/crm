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


    def __str__(self):
        return f'{self.first_name} {self.last_name} (id: {self.id})'