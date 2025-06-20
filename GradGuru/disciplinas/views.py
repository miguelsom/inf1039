from django.shortcuts import render, get_object_or_404
from .models import Disciplina

def lista_disciplinas(request):
    disciplinas = Disciplina.objects.all()
    return render(request, 'disciplinas.html', {'disciplinas': disciplinas})

def pag_disciplina(request, codigo):
    disciplina = get_object_or_404(Disciplina, codigo__iexact=codigo)
    return render(request, 'pag_disciplina.html', {'disciplina': disciplina})
