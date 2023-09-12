from django.db import models

# Create your models here.

class Institute(models.Model):
    Name= models.CharField(max_length=50, primary_key=True)
    Student= models.CharField(max_length=50)
    ID= models.IntegerField()
    Email= models.EmailField()
    RenterMail= models.EmailField()
    Date= models.DateField()
    Contact= models.CharField(max_length=10)