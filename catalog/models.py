
from django.db import models

class Brand(models.Model):
	brand_name = models.CharField(max_length=50)
	def __str__(self):
		return self.brand_name

# Create your models here.
class Product(models.Model):
	name = models.CharField(max_length=50)
	price = models.DecimalField(max_digits=6,decimal_places=2)
	brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
	date_of_receipt = models.DateTimeField('date of receipt')

	def __str__(self):
		return self.name
