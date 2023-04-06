from django.db import models

class SensorData(models.Model):
    topic = models.CharField(max_length=50)
    value = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
