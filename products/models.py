from django.db import models
from stores.models import Store
from categories.models import Category
# Create your models here.
class Product(models.Model):
    name = models.TextField()
    price = models.IntegerField()
    store = models.ForeignKey(Store, on_delete=models.CASCADE)

class ProductCategory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)