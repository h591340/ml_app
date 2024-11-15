from django.db import models

# Create your models here.
class Employee(models.Model):
    age = models.IntegerField()
    gender = models.CharField(max_length=255)
    educationLevel =  models.CharField(max_length=255)
    jobTitle = models.TextField(blank=True)
    yearsOfExperience =  models.IntegerField()
    salary = models.FloatField()
    def __str__(self):
        return self.jobTitle+" " +str(self.salary)
    
