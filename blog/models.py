from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    body = models.CharField(max_length=10000)
    image = models.ImageField(upload_to='images/')
    