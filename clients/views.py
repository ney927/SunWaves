from django.shortcuts import render, redirect
from clients.forms import clientForm, addIndustry, addPosition
from clients.models import client
# Create your views here.
def create_client_view(request):
  form = clientForm()
  if request.method == 'POST':
    form = clientForm(request.POST)
    if form.is_valid():
      # form.save()
      return redirect('home')
  context = {
    'form': form,
  }
  return render(request, 'clientForm.html', context)

def home_view(request):
  context = {}
  return render(request, 'base.html', context)

def search_view(request):
  cl = client.objects.all()
  context= {
    'clients': cl
  }
  return render(request, 'searchClients.html', context)
