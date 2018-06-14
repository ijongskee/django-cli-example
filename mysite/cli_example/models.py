import datetime
from django.db import models
from django.utils import timezone

class City(models.Model):
	city = models.CharField(max_length=200)
	date_created = models.DateTimeField("date created")

	def __str__(self):
		return self.city

	def was_published_recently(self):
		return self.date_created >= timezone.now() - datetime.timedelta(days-1)

class Baranggay(models.Model):
	city = models.ForeignKey(City, on_delete=models.CASCADE)
	baranggay = models.CharField(max_length=200)
	baranggay_date_created = models.DateTimeField("date_created")
	def __str__(self):
		return self.baranggay

class Resident(models.Model):
	
	first_name = models.CharField(max_length=200)
	middle_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	city = models.ForeignKey(City, on_delete=models.CASCADE)
	baranggay = models.ForeignKey(Baranggay, on_delete=models.CASCADE)
	street = models.CharField(max_length=200)
	house_no = models.CharField(max_length=200)

	resident_date_created = models.DateTimeField("date_created")
	def __str__(self):
		return self.first_name
	

	