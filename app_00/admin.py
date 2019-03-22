from django.contrib import admin
from app_00.models import BookShop, Book, Order

# Register your models here.
admin.site.register(BookShop)
admin.site.register(Book)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'book',
        'name',
        'phone',
        'date',

    ]
