from django import forms

JOBS = (
  ("Python", "Python Developper"),
    ("Java", "Java Developper"),
    ("JavaScript", "JavaScript Developper")
)

class SignupForm(forms.Form):
    pseudo = forms.CharField(max_length=8, required=False)
    email = forms.CharField()
    password = forms.CharField(min_length=6)
    job = forms.ChoiceField(choices=JOBS)
    cgu_accept = forms.BooleanField(initial=True)

CITIES = (
  ('Tanger', 'Capitale du nord'),
  ('Fes', 'Capitale culturelle'),
  ('Rabat', 'Capitale administrative'),
  ('Casablanca', 'Capitale economique')
)

LANGUAGES=(
  ('Ar', 'Arabic'),
  ('Fr', 'French'),
  ('En', 'English'),
  ('Sp', 'Spanish')
)

class SignupFormWidget(forms.Form):
  pseudo = forms.CharField(max_length=8, required=False)
  email = forms.EmailField()
  password = forms.CharField(min_length=6, widget=forms.PasswordInput)
  jobs = forms.ChoiceField(choices=JOBS, widget=forms.RadioSelect)
  city = forms.ChoiceField(choices=CITIES, widget=forms.CheckboxSelectMultiple)
  language = forms.MultipleChoiceField(choices=LANGUAGES, widget=forms.SelectMultiple)
  cgu_accept = forms.BooleanField(initial=True)

class SignupFormData(forms.Form):
  pseudo = forms.CharField(max_length=8, required=False)
  email = forms.EmailField()
  password = forms.CharField(min_length=6, widget=forms.PasswordInput)
  jobs = forms.ChoiceField(choices=JOBS, widget=forms.RadioSelect)
  language = forms.MultipleChoiceField(choices=LANGUAGES, widget=forms.CheckboxSelectMultiple)
  cgu_accept = forms.BooleanField(initial=True)