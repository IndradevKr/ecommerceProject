from django.contrib import admin

# Register your models here.
from .models import Product, Contact, Order, orderUpdate
from django.contrib.auth.models import User
admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(Order)
admin.site.register(orderUpdate)



