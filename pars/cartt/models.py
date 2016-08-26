from __future__ import unicode_literals

from django.db import models
from parsxlx.models import Workbook

# Create your models here.
class Cart(models.Model):
	product = models.ForeignKey(Workbook)
	quantity = models.CharField(max_length=100)
	date_of_buy = models.DateTimeField(default=timezone.now())

class CartOfUser(models.Model):
	user = models.OneToOneField(User, related_name='cart')
	product_of_cart = models.ManyToManyField(Cart, blank=True, null=True, related_name='prof')
