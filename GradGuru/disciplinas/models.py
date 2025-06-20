from account.models import Profile
from django.db import models

class Disciplina(models.Model):
    codigo = models.CharField(primary_key=True, max_length=20)
    nome = models.CharField(max_length=100)
    departamento = models.CharField(max_length=100)
    graduacao = models.CharField(max_length=100, blank=True, null=True)
    tipo = models.CharField(max_length=20, choices=[
        ("Obrigatória", "Obrigatória"),
        ("Eletiva", "Eletiva")
    ], blank=True, null=True)

    materiais = models.TextField(blank=True)
    professores = models.ManyToManyField(
        Profile,
        related_name='disciplinas',
        limit_choices_to={'role': 'teacher'}
    )
    pre_requisitos = models.ManyToManyField(
        'self',
        symmetrical=False,
        blank=True,
        related_name='disciplinas_requeridas'
    )

    def __str__(self):
        return f'{self.nome} ({self.codigo})'
