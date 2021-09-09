from django.db import models

# Create your models here.
class Lesson(models.Model):
    name = models.CharField(max_length=100)
    time = models.DateTimeField(null=True, blank=True)
    image = models.ImageField(upload_to='images/')