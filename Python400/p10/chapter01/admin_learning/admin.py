from django.contrib import admin
from .models import *


@admin.register(Waiter)
class WaiterAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'sex']
    ordering = ['age']


# Register your models here.
admin.site.register(Place)
admin.site.register(Restaurant)
# admin.site.register(Waiter, WaiterAdmin)
