from django.contrib import admin
from warehouse.models import Product, Supplier, Recipient, Booking, Ship, SupplyAvailability


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'description'
    )
    search_fields = ('name',)
    ordering = ('id',)
    # list_filter = ('is_pep', 'pep_type', 'is_dead')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        'booking_date',
        'product',
        'recipient'
    )
    search_fields = ('recipient',)
    ordering = ('booking_date',)


@admin.register(Ship)
class ShipAdmin(admin.ModelAdmin):
    list_display = (
        'ship_date',
        'product',
        'recipient'
    )
    search_fields = ('recipient',)
    ordering = ('ship_date',)


@admin.register(SupplyAvailability)
class SupplyAvailabilityAdmin(admin.ModelAdmin):
    list_display = (
        'supply_date',
        'product',
        'supplier',
        'booking',
        'ship'
    )
    search_fields = ('supplier',)
    ordering = ('supply_date',)


admin.site.register(
    [
        Supplier,
        Recipient,
    ]
)
