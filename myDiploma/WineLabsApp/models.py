from django.db import models

class Wine(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='images/wines/')
    keywords = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name



