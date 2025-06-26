from django.urls import path
from . import views

app_name = 'avaliacoes'

urlpatterns = [
    path('disciplina/<str:codigo>/avaliacoes/', views.listar_avaliacoes_disciplina, name='listar_avaliacoes_disciplina'),
    path('disciplina/<str:codigo>/avaliar/', views.avaliar_disciplina, name='avaliar_disciplina'),
]
