from django.db import models

class Game(models.Model):
    name = models.CharField(max_length=120)
    genre = models.CharField(max_length=120)
    sales_price = models.DecimalField(max_digits=5, decimal_places=2)
    vendor_cost = models.DecimalField(max_digits=5, decimal_places=2)
    threshold = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name