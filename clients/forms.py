from django import forms
from .models import client, industryChoices, positionChoices

class clientForm(forms.ModelForm):
  class Meta:
    model = client
    fields = [
      'name',
      'country',
      # 'residence',
      # 'status',
      'email',
      'phone_number',
      'experience',
      'industry',
      'position',
      'education',
      'resume',
    ]

class addIndustry(forms.ModelForm):
  class Meta:
    model = industryChoices
    fields = [
      'ind'
    ]

class addPosition(forms.ModelForm):
  class Meta:
    model = positionChoices
    fields = [
      'pos'
    ]
