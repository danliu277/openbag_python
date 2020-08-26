from django.db import models

class Sale(models.Model):
    customer_id = models.IntegerField()
    game_id = models.IntegerField()
    employee_id = models.IntegerField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.name