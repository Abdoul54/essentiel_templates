from django.shortcuts import render
from .forms import SignupForm
# Create your views here.

def signup10_affichage(request):
  form = SignupForm()
  return render(request, 'myform_form/signup10_affichage.html', context={'form': form})