from django.db import models


# Create your models here.

class Groups(models.Model):
    GroupsId = models.AutoField(primary_key=True)
    GroupName = models.CharField(max_length=100, unique=True)


class StatusCatalogs(models.Model):
    CatalogId = models.AutoField(primary_key=True)
    DescriptionName = models.CharField(max_length=100)


class Customers(models.Model):
    CustomerId = models.AutoField(primary_key=True)
    CustomerName = models.CharField(max_length=100)
    CustomerName2 = models.CharField(max_length=100, blank=True, null=True)
    CustomerName3 = models.CharField(max_length=100, blank=True, null=True)
    Surname = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100, null=True)
    DateOfJoining = models.DateField(blank=True, null=True)
    Street = models.CharField(max_length=100, blank=True, null=True)
    Number = models.CharField(max_length=100, blank=True, null=True)
    Suburb = models.CharField(max_length=100, blank=True, null=True)
    ZipCode = models.CharField(max_length=100, blank=True, null=True)
    PhotoFileName = models.CharField(max_length=100, blank=True, null=True)
    Status = models.CharField(max_length=100, blank=True, null=True, default='0')
    StatusBC = models.CharField(max_length=100, blank=True, null=True)
    StatusWL = models.CharField(max_length=100, blank=True, null=True)
    StatusPLD = models.CharField(max_length=100, blank=True, null=True)
    Group = models.CharField(max_length=100, null=True, blank=True)

