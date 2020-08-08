from django.contrib import admin
from .models import *


def age_plus_one(modeladmin, request, queryset):
    queryset.update(age=models.F('age')+1)
    age_plus_one.short_description = '年龄加1'


@admin.register(Waiter)
class WaiterAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'sex']
    ordering = ['age']
    actions = [age_plus_one]


# Register your models here.
admin.site.register(Place)
admin.site.register(Restaurant)
# admin.site.register(Waiter, WaiterAdmin)
