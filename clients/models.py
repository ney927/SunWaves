from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class client(models.Model):
  name = models.CharField()
  country = models.CharField()

