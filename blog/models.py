from django.db import models
from django.utils import timezone

class Product(models.Model):

	name = models.CharField(max_length=100, default='')
	
	price = models.PositiveIntegerField(default=0)
	image = models.FileField(upload_to="img/")
	def __str__(self):
		return str(self.id)


class Payment(models.Model):
	cost = models.PositiveIntegerField(default=0)
	date = models.DateTimeField()
	payment_type = models.PositiveIntegerField(default=0)
	user = models.ForeignKey('auth.User')
	def _str_(self):
		return str(self.id)