from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from .forms import SignupForm, SignupFormWidget, SignupFormData
# Create your views here.

def signup10_affichage(request):
  form = SignupForm()
  return render(request, 'myform_form/Signup10_affichage.html', context={'form': form})

def signup20_widget(request):
  form = SignupFormWidget()
  return render(request, 'myform_form/Signup20_widget.html', context={'form': form})

def signup30_data(request):
  if request.method == 'POST':
    form = SignupFormData(request.POST)
    if form.is_valid():
      cd = form.cleaned_data
      return redirect(reverse("signup30_reussi"))
  else:
    form = SignupFormData()
  return render(request, 'myform_form/signup30_data.html', context={'form': form})

def signup30_reussi(request):
  return render(request, 'myform_form/signup30_reussi.html')

def signup31_data(request):
  form = SignupFormData()
  return render(request, "myform_form/signup31_data.html", context={"form":form})

def signup31_affichage(request):
  form = SignupFormData(request.POST)
  if form.is_valid():
    cd = form.cleaned_data
    print(cd)
    return render(request, "myform_form/signup31_affichage.html", {"cd":cd})
  else:
    return HttpResponse("Les données ne sont pas valides")
