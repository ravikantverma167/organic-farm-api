from django.db import models

# Create your models here.


class Categories(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    description = models.TextField(max_length=1000, null=True)
    pic_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Products(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    description = models.TextField(max_length=1000)
    pic_url = models.URLField(blank=True, null=True)
    price_value = models.IntegerField(max_length=100000, default=None)
    price_currency = models.CharField(max_length=20,default=None)
    dimension_value = models.IntegerField(max_length = 1000, default=None)
    dimension_unit = models.CharField(max_length=20,null=True)
    category = models.CharField(max_length= 250)
    created_at = models.DateTimeField(auto_now_add=True)