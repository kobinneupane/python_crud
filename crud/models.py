from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length = 100)
    roll_number = models.CharField(max_length = 200)
    age = models.IntegerField()
    
    def __str__(self) -> str:
        return f"{self.name}"
    
class Teacher(models.Model):
    name = models.CharField(max_length = 100)
    address = models.CharField(max_length = 100)
    salary = models.IntegerField()
    
    def __str__(self) -> str:
        return f"{self.name}"


