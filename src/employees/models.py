from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=120)
    username = models.CharField(max_length=120)
    password = models.CharField(max_length=120)
    address = models.CharField(max_length=120)
    email = models.CharField(max_length=120)

    def __str__(self):
        return self.name