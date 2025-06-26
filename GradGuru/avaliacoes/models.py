from django.db import models
from account.models import Profile
from disciplinas.models import Disciplina
from django.core.validators import MinValueValidator, MaxValueValidator

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
    pontuacao = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)],
        help_text="Pontuação de 0 a 5"
    )
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Avaliação de {self.disciplina} por {self.aluno} - Pontuação: {self.pontuacao} - Data: {self.data.strftime("%d/%m/%Y %H:%M")}'
