from django.shortcuts import render, redirect
from clients.forms import clientForm
from .model_choices import industry_choices, position_choices
from clients.models import client
choices = ['apples', 'oranges']
# Create your views here.
def create_client_view(request):
  form = clientForm()
  ind = request.POST.get('ind')
  pos = request.POST.get('pos')
  if request.method == 'POST':
    form = clientForm(request.POST)
    if form.is_valid():
      if form.cleaned_data['industry'] == 'Other':
        industry_choices.append(ind)
        choices.append(ind)
        print(choices)
        form.cleaned_data['industry'] = ind
      if form.cleaned_data['position'] == 'Other':
        position_choices.append(pos)
        form.cleaned_data['position'] = pos
      print(form.cleaned_data)
      print(form.cleaned_data['industry'])
      print(form.cleaned_data['position'])
      # form.save()
      client.objects.create(
        name = form.cleaned_data['name'],
        country = form.cleaned_data['country'],
        email = form.cleaned_data['email'],
        phone_number = form.cleaned_data['phone_number'],
        experience = form.cleaned_data['experience'],
        industry = ind,
        position= pos,
        education = form.cleaned_data['education']
      )
      return redirect('home')
  context = {
    'form': form,
    'choices': choices
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
