from django.contrib import admin

from dashboard.models import Customer, Payment, Task

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    pass


class PaymentAdmin(admin.ModelAdmin):
    pass

class TaskAdmin(admin.ModelAdmin):
    pass

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(Task, TaskAdmin)