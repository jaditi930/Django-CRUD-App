from django.db import models
from datetime import datetime
# Create your models here.
class Flights(models.Model):
    start_point=models.CharField(max_length=120)
    dest=models.CharField(max_length=120)
    timing=models.DateTimeField(default=datetime.now)