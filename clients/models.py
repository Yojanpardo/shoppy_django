from django.db import models

# Create your models here.

class Client(models.Model):
	first_name = models.CharField(max_length=60)
	last_name = models.CharField(max_length=60)
	gender = models.CharField(max_length=15)
	cellphone = models.CharField(max_length=11)
	cedula = models.CharField(max_length=11, unique=True)
	email = models.EmailField(max_length=90, unique=True)
	birthday = models.DateField()

	def __str__(self):
		return self.first_name

	class Meta:
		ordering = ('id',)