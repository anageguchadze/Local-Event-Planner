from django.db import models

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    date = models.CharField(max_length=50)
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.title