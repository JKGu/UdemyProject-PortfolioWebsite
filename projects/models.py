from django.db import models

class Project(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=1000)

    def __str__(self):
        return self.summary[:25]