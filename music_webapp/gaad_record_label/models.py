from django.db import models

# Create your models here.


class Artist(models.Model):
    name = models.CharField(max_length=100)
    about = models.TextField()
    nationality = models.CharField(max_length= 50)
    location = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pics')
