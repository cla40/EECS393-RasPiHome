from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=18)
    password = models.CharField(max_length=18)
    email = models.EmailField(max_length=100)
    sQuestion = models.CharField(max_length=100)
    sAnswer = models.CharField(max_length=50)
    lastAddress = models.IPAddressField()
    userID = models.PositiveIntegerField(primary_key=True)
class Alarm(models.Model):
    username = models.CharField(max_length=18) #Creators Username
    alarmID = models.PositiveIntegerField(primary_key=True)
    buildingID = models.ForeignKey('Building') #Foreign Key
    outletID = models.ForeignKey('Outlet') #Foreign Key
    alarmName = models.CharField(max_length=25)
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()
    desiredState = models.BooleanField()
    #For a timer startTime is NULL and endTime will be used to calculate the duration
class Building(models.Model):
    buildingname = models.CharField(max_length=18)
    buildingID = models.PositiveIntegerField(primary_key=True)
    userID = models.ForeignKey('User') #Foreign Key
class Outlet(models.Model):
    outletID = models.PositiveIntegerField(primary_key=True)
    buildingID = models.ForeignKey('Building') #Foriegn Key
    state = models.BooleanField()
