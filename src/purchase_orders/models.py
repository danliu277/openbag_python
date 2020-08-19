from django.db import models

class PurchaseOrder(models.Model):
    game_id = models.IntegerField()
    employee_id = models.IntegerField()
    vendor_id = models.IntegerField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.name