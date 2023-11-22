from django.db import models

class Product(models.Model):
    sku = models.TextField()
    description = models.TextField()
    qtyperpcs = models.IntegerField()
    bccs =  models.TextField()
    bcib =  models.TextField()
    bcpcs =  models.TextField()

    def __str__(self):
        return self.sku
