from django.db import models
from django.db.models.fields import CharField
from .model_choices import position_choices, industry_choices, education_choices

# Create your models here.
class client(models.Model):
  name = models.CharField(max_length=100)
  country = models.CharField(max_length=100)
  email = models.EmailField(max_length=100)
  phone_number = models.CharField(max_length=50)
  experience = models.IntegerField()
  industry = models.CharField(max_length=100, choices=industry_choices)
  position = models.CharField(max_length=100, choices=position_choices)
  education = models.CharField(max_length=100, choices=education_choices)

  def __str__(self):
      return f'{self.name}'

