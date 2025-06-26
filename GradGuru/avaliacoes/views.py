from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib import messages
from .models import AvaliacaoDisciplina
from .forms import AvaliacaoDisciplinaForm
from disciplinas.models import Disciplina
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods

# Create your views here.

@require_http_methods(["GET"])
def listar_avaliacoes_disciplina(request, codigo):
    disciplina = get_object_or_404(Disciplina, codigo=codigo)
    avaliacoes = AvaliacaoDisciplina.objects.filter(disciplina=disciplina)
    data = [
        {
            'aluno': avaliacao.aluno.user.username,
            'pontuacao': avaliacao.pontuacao,
            'avaliacao': avaliacao.avaliacao,
            'data': avaliacao.data.strftime('%d/%m/%Y %H:%M'),
        }
        for avaliacao in avaliacoes
    ]
    return JsonResponse({'avaliacoes': data})

@login_required
@require_http_methods(["GET", "POST"])
def avaliar_disciplina(request, codigo):
    disciplina = get_object_or_404(Disciplina, codigo=codigo)
    if request.method == 'POST':
        form = AvaliacaoDisciplinaForm(request.POST)
        if form.is_valid():
            avaliacao = form.save(commit=False)
            avaliacao.aluno = request.user.profile
            avaliacao.disciplina = disciplina
            avaliacao.save()
            messages.success(request, 'Avaliação enviada com sucesso!')
            return redirect('disciplinas:pag_disciplina', codigo=disciplina.codigo)
    else:
        form = AvaliacaoDisciplinaForm()
    return render(request, 'avaliacoes/avaliar_disciplina.html', {'form': form, 'disciplina': disciplina})
