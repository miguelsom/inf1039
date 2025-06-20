from django.urls import path
from . import views

app_name = "disciplinas"

urlpatterns = [
    path("", views.lista_disciplinas, name="lista_disciplinas"),
    path("<str:codigo>/", views.pag_disciplina, name="pag_disciplina"),
]
