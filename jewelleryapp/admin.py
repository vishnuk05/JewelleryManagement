from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(customer_table)
admin.site.register(staff_table)
admin.site.register(products)