from django.db import models

# Create your models here.
class imgData(models.Model):
    img = models.ImageField(upload_to='img/')
    dateandtime = models.DateTimeField(auto_now_add=True)