from django.db import models
from account.models import Profile
from disciplinas.models import Disciplina

class AvaliacaoDisciplina(models.Model):
    aluno = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'student'},
        related_name='avaliacoes_disciplinas'
    )
    disciplina = models.ForeignKey(
        Disciplina,
        on_delete=models.CASCADE,
        related_name='avaliacoes'
    )
    avaliacao = models.TextField()

    def __str__(self):
        return f'Avaliação de {self.disciplina} por {self.aluno}'
