from django.db import models

# Create your models here. Developed by Yojan Pardo

class Product(models.Model):
	name = models.CharField(max_length=255)
	description = models.CharField(max_length=255)
	category = models.CharField(max_length=255)
	price = models.DecimalField(max_digits=11, decimal_places=2)
	image = models.ImageField(blank=True)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ('id',)