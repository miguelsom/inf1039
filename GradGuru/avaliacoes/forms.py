from django import forms
from .models import AvaliacaoDisciplina

class AvaliacaoDisciplinaForm(forms.ModelForm):
    class Meta:
        model = AvaliacaoDisciplina
        fields = ['disciplina', 'avaliacao', 'pontuacao']
        widgets = {
            'avaliacao': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Escreva sua avaliação...'}),
            'pontuacao': forms.NumberInput(attrs={'min': 0, 'max': 5}),
        } 