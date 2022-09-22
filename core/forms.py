from dataclasses import fields
from pyexpat import model
from django import forms
from .models import Produto, Funcionario
from django.contrib.auth.models import User
from .widgets import CustomDateWidget


class CadastrarProdutoForm(forms.Form):
    marca = forms.CharField(max_length=100)
    modelo = forms.CharField(max_length=100)
    lote = forms.CharField(max_length=100)
    preco = forms.FloatField()
    
    
class CadastrarMonitorForm(CadastrarProdutoForm):
    tamanho = forms.IntegerField()
    taxa_de_atualizacao = forms.IntegerField()
    resolucao = forms.CharField(max_length=15)
    tipo_de_tela = forms.CharField(max_length=10)
    
    
class CadastrarComputadorForm(CadastrarProdutoForm):
    memoria_ram = forms.IntegerField()
    armazenamento = forms.IntegerField()
    sistema_operacional = forms.CharField(max_length=50) 

class CadastrarUsuarioForm(forms.Form):
    nome_usuario = forms.CharField(max_length=100)
    nome = forms.CharField(max_length=100)
    senha = forms.CharField(max_length=100, widget=forms.PasswordInput())
    email = forms.EmailField()

    def save(self) -> User:
        clean_form = self.cleaned_data
        return User.objects.create_user(
            username = clean_form.get('nome_usuario'),
            first_name = clean_form.get('nome'),
            password = clean_form.get('senha'),
            email = clean_form.get('email')
        )
    
class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput())


class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = '__all__'
        widgets = {
            'data_de_admissao': CustomDateWidget(),
        }