from django.shortcuts import render
from clients.forms import clientForm

# Create your views here.
def create_client_view(request):
  form = clientForm()
  context = {
    'form': form,
  }
  return render(request, 'clientForm.html', context)

def home_view(request):
  context = {}
  return render(request, 'base.html', context)