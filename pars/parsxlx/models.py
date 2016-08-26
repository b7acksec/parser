from __future__ import unicode_literals

from django.db import models

USD = 67

# Create your models here.
class Workbook (models.Model):
	title = models.CharField(max_length=255, null=True, blank=True)
	price = models.CharField(max_length=20, null=True, blank=True)
	som = models.CharField(max_length=200)

	def get_som(self):
		try:
			return float(self.price) * USD
		except Exception:
			return 'NONE'

	def __str__(self):
		return self.title



	# def __init__ (self, name, price)
	# self.name = 
	# self.price = 