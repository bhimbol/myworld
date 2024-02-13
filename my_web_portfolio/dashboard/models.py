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

class Promo(models.Model):
    sku = models.TextField()
    child_sku = models.TextField()
    mech_per_pcs = models.IntegerField()
    related_product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='promos', null=True, blank=True)
    def __str__(self):
        return self.sku

class Valuation(models.Model):
    sku = models.TextField()
    description = models.TextField()
    cs = models.IntegerField()
    ib =  models.IntegerField()
    pcs =  models.IntegerField()
    def __str__(self):
        return self.sku
