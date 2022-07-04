from telnetlib import STATUS
from django.db import models


class Quotation(models.Model):

	STATUS =(
			('Pending', 'Pending'),
			('Out For Delivery', 'Out For Delivery'),
			('Delivered', 'Delivered'),
			('Done Service', 'Done Service'),
			('On going', 'On going'),
			)

	date = models.DateTimeField(auto_now_add=True, null=True)
	company_name = models.CharField(max_length=200, null=True)
	address = models.CharField(max_length=200, null=True)
	purchasing_officer = models.CharField(max_length=200, null=True)
	eic = models.CharField(max_length=200, null=True)
	subject = models.CharField(max_length=200, null=True)
	project_name = models.CharField(max_length=200, null=True)
	price = models.FloatField(null=True)
	top = models.CharField(max_length=200, null=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS)


	def __str__(self):
		return self.company_name


class Code(models.Model):
	codex = models.CharField(max_length=200, null=True)
	

	def __str__(self):
		return self.company_name
