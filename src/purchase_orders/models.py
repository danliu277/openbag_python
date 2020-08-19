from django.db import models

class PurchaseOrder(models.Model):
    game_id = stock = models.IntegerField()
    employee_id = stock = models.IntegerField()
    vendor_id = stock = models.IntegerField()
    quantity = stock = models.IntegerField()

    def __str__(self):
        return self.name