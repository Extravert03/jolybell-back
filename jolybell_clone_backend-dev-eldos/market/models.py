from django.db import models

from . import helpers


class ProductCategory(models.Model):
    name = models.CharField(max_length=64, unique=True)

    class Meta:
        verbose_name_plural = 'Product categories'
        verbose_name = 'Product category'

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.PROTECT)
    name = models.CharField(max_length=128)
    price = models.FloatField()
    stocks = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    discount = models.FloatField()
    description = models.TextField()
    image = models.ImageField(upload_to=helpers.RandomFileName(''))

    def __str__(self):
        return f'{self.category.name} | {self.name}'
