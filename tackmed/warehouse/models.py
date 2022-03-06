from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=500)
    description = models.CharField(max_length=3000)

    def __str__(self):
        return self.name


class Supplier(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Recipient(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Booking(models.Model):
    recipient = models.ForeignKey(Recipient, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    booking_date = models.DateTimeField('booking date')

    # def __str__(self):
    #     return self.recipient


class Ship(models.Model):
    recipient = models.ForeignKey(Recipient, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    ship_date = models.DateTimeField('ship date')


class SupplyAvailability(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    supply_date = models.DateTimeField('supply date')
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, null=True, blank=True)
    ship = models.ForeignKey(Ship, on_delete=models.CASCADE, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.booking:
            self.booking = None
        if not self.ship:
            self.ship = None
        super(SupplyAvailability, self).save(*args, **kwargs)
