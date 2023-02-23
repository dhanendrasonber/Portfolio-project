from django.db import models

# Create your models here.
class ContactMe(models.Model):
    Name=models.CharField(max_length=50)
    Email=models.EmailField(max_length=50)
    Phone=models.CharField(max_length=50)
    Concern=models.CharField(max_length=50)

def __str__(self) -> str:
    return self.Name
    
     