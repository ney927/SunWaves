from django.shortcuts import render, redirect
from clients.forms import clientForm, addIndustry, addPosition
from clients.models import client, industryChoices, positionChoices
# Create your views here.
def create_client_view(request):
  form = clientForm()
  if request.method == 'POST':
    form = clientForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
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
  if request.method == 'POST':
    ind = request.POST.get('searchIND')
    pos = request.POST.get('searchPOS')
    edu = request.POST.get('searchEDU')
    exp = request.POST.get('searchEXP')
    return redirect('results', ind, pos, edu, exp)
  context= {
    'clients': cl,
  }
  return render(request, 'searchClients.html', context)

def search_results_view(request, ind, pos, edu, exp):
  query = client.objects.all()
  if ind != 'Any':
    query = query.filter(industry__ind=ind)
  context = {
    'query': query
  }
  return render(request, 'searchResults.html', context)


def add_options_view(request):
  Iform = addIndustry()
  Pform = addPosition()
  if request.method=='POST':
    newInd = request.POST.get('ind')
    newPos = request.POST.get('pos')
    if newInd is not None:
      industryChoices.objects.create(ind = newInd)
    if newPos is not None:
      positionChoices.objects.create(pos=newPos)
  context = {
    'Iform': Iform,
    'Pform': Pform,
  }
  return render(request, 'addOptions.html', context)
