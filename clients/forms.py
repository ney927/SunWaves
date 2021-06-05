from django import forms
from .models import client

class clientForm(forms.ModelForm):
  class Meta:
    model = client
    fields = [
      'name',
      'country',
      'email',
      'phone_number',
      'experience',
      'industry',
      'position',
      'education',
    ]