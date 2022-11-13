from django.db import models

class Emp(models.Model):
	num = models.IntegerField()
	name = models.CharField(max_length=30)
	salary = models.FloatField()
	address = models.CharField(max_length=50)

	def __str__(self):
		return self.name