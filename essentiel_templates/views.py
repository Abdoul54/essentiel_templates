from django.shortcuts import render
import datetime
from . import Utilataires
def index(request):
    return render(request, 'index.html')

def view_static(request):
    return render(request, 'temp_static.html')

def view_variables(request):
    vint = 10
    vfloat = 10.5
    vbool = True
    vstring = 'Bonjour'
    vdate = datetime.datetime.today()
    dictionnaire = {'vint': vint, 'vfloat': vfloat, 'vboolean': vbool, 'vstring': vstring, 'vdate': vdate}
    return render(request, 'temp_variables.html', context=dictionnaire)

def view_attributs(request):
    etudiant = Utilataires.Etudiant("Etud001", "Bahroune", "Said", "M", 12.5)
    context = {"etudiant":etudiant}
    return render(request, 'temp_attributsObjet.html', context)

def view_alternative(request):
    etudiant = Utilataires.Etudiant("Etud001", "Chamsoune", "Meryem", "F", 19.5)
    context = {"etudiant":etudiant}
    return render(request, 'temp_alternative.html', context)

def view_boucle(request):
    classe = []
    classe.append(Utilataires.Etudiant("Etud001", "Bardoune", "Najib", "M", 12.5))
    classe.append(Utilataires.Etudiant("Etud002", "Naimoune", "Ali", "M", 8.5))
    classe.append(Utilataires.Etudiant("Etud003", "Misbahoune", "Nadia", "F", 15.5))
    classe.append(Utilataires.Etudiant("Etud004", "Chamsoune", "Meryem", "F", 19.5))
    classe.append(Utilataires.Etudiant("Etud005", "Mardiyoune", "Fouad", "M", 13.5))
    classe.append(Utilataires.Etudiant("Etud006", "Mouttakioune", "Said", "M", 10.5))
    s = 0
    for etudiant in classe:
        s += etudiant.note
    moyenne = round(s/len(classe), 2)
    classe_vide = []
    context = {"classe":classe, "moyenne":moyenne, "classe_vide":classe_vide}


    return render(request, 'temp_boucle.html', context)

def view_heritage(request):
    return render(request, 'temp_heritage.html')