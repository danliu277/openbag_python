from django.db import models

class Game(models.Model):
    name = models.CharField(max_length=120)
    genre = models.CharField(max_length=120)
    sales_price = models.DecimalField(decimal_places=2)
    vendor_cost = models.DecimalField(decimal_places=2)
    threshold = models.DecimalField(decimal_places=2)

    def __str__(self):
        return self.name