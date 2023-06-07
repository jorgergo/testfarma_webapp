from django.db import models

# Create your models here.

class Subsidiary(models.Model):
    
    name = models.CharField(max_length=100)
    
    address = models.CharField(max_length=35)

class Study(models.Model):
    
    name = models.CharField(max_length=100)
    
    description = models.CharField(max_length=160)
    
    previousIndications = models.CharField(max_length=100)

class Appointment(models.Model):
    
    place = models.CharField(max_length=100)
    
    study = models.CharField(max_length=100)
    
    date = models.DateField()
    
    hour = models.TimeField()
    

class State(models.Model):
    state = models.CharField(max_length=50)
    code = models.IntegerField()
    contraction = models.CharField(max_length=2)
    def __str__(self):
        return self.state 
    
class Town(models.Model):
    town = models.CharField(max_length=50)
    code = models.CharField(max_length=4)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    def __str__(self):
        return self.town 
    
    
    
    