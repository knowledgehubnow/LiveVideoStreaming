from django.db import models

# Create your models here.
class LiveStream(models.Model):
    room = models.CharField(max_length= 50)
    is_streaming = models.BooleanField(default=True)