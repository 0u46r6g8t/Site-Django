from django import forms
from django.forms.widgets import ClearableFileInput
from core.models import Produtos

class ProdutoModelForm(forms.ModelForm):
    photo = forms.ImageField(widget=ClearableFileInput)

    class Meta:
        model = Produtos
        fields = '__all__' # Quer dizer que irá usar todos os campus
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'maxlength':255,
                'placeholder': 'Digite o nome do produto'
            }),
            'descrition': forms.Textarea(attrs={
                'class':'forms-control'
            })
        }

        error_message = {
            'nome': {
                'required': 'Este campo é obrigatório'
            },
            'descrition': {
                'required': 'Este campo é obrigatório'
            }
        }