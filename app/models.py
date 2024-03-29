from django.db import models

# Create your models here.
class Prodectcatogury(models.Model):
    prod_id=models.IntegerField(primary_key=True)
    prod_name=models.CharField(max_length=100)

    def __str__(self):
        return self.prod_name

class Product(models.Model):
    prod_id=models.ForeignKey(Prodectcatogury,on_delete=models.CASCADE)
    product_id=models.IntegerField()
    product_name=models.CharField(max_length=100)
    product_prize=models.IntegerField()
    