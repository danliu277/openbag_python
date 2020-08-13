from django.db import models

class Article(models.Model):
    name = models.CharField(max_length=120)
    address = models.CharField(max_length=120)
    email = models.CharField(max_length=120)

    def __str__(self):
        return self.name