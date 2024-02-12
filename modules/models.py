# product_management/models.py

from django.db import models

class Product_mst(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100)

class Product_sub_cat(models.Model):
    product = models.ForeignKey(Product_mst, on_delete=models.CASCADE)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_image = models.ImageField(upload_to='product_images/')
    product_model = models.CharField(max_length=100)
    product_ram = models.IntegerField()
