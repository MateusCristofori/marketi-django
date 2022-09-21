from django import forms
from .models import Produto


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
    
class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput())