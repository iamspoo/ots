from django.contrib import admin

from .models import customer
from .models import order

admin.site.register(customer)
admin.site.register(order)
