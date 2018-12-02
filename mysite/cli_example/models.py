from django.db import models
from django.utils import timezone
    

class Baranggay(models.Model):
    name = models.CharField(max_length=200)
    date_created = models.DateTimeField("date_created")
    def __str__(self):
        return self.name
    
    
class City(models.Model):
    name = models.CharField(max_length=200)
    baranggay = models.ForeignKey(Baranggay, on_delete=models.CASCADE, null=True, blank=True)
    date_created = models.DateTimeField("date_created")

    def __str__(self):
        return self.name


class Province(models.Model):
    name = models.CharField(max_length=200)
    date_created = models.DateTimeField("date_created")
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class Region(models.Model):
    name = models.CharField(max_length=200)
    date_created = models.DateTimeField("date_created")
    province = models.ForeignKey(Province, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

        
class Island(models.Model):
    name = models.CharField(max_length=200)
    date_created = models.DateTimeField("date_created")
    region = models.ForeignKey(Region, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

        
class Country(models.Model):
    name = models.CharField(max_length=200)
    island = models.ForeignKey(Island, on_delete=models.CASCADE, null=True, blank=True)
    date_created = models.DateTimeField("date_created")

    def __str__(self):
        return self.name

        
class Resident(models.Model):
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True, blank=True)
    island = models.ForeignKey(Island, on_delete=models.CASCADE, null=True, blank=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, null=True, blank=True)
    province = models.ForeignKey(Province, on_delete=models.CASCADE, null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    baranggay = models.ForeignKey(Baranggay, on_delete=models.CASCADE)
    street = models.CharField(max_length=200)
    house_no = models.CharField(max_length=200)
    date_created = models.DateTimeField("date_created")
    
    def __str__(self):
        return self.first_name


            

