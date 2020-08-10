from django.contrib import admin

from dashboard.models import Customer

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    pass

admin.site.register(Customer, CustomerAdmin)