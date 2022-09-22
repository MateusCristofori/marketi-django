from django.shortcuts import render, redirect
from django import views
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from ..forms import CadastrarProdutoForm, CadastrarUsuarioForm, LoginForm, CadastrarComputadorForm, CadastrarMonitorForm, FuncionarioForm
from ..models import Produto


class CadastrarView(views.View):
    
    forms = {
        'produto': CadastrarProdutoForm,
        'computador': CadastrarComputadorForm,
        'monitor': CadastrarMonitorForm,
        'funcionario': FuncionarioForm
    }
    
    def get(self, request, tipo):
        form = self.forms[tipo]()
        
        context = {
            'form': form
        }
        return render(request, 'formularios/formulario_generico.html', context)
    
    def post(self, request, tipo):
        form = self.forms[tipo](request.POST)
        
        if form.is_valid():
            form_limpo = form.cleaned_data
            marca = form_limpo.get('marca')
            modelo = form_limpo.get('modelo')
            lote = form_limpo.get('lote')
            preco = form_limpo.get('preco')
            Produto.objects.create(
                marca=marca,
                modelo=modelo,
                lote=lote,
                preco=preco
            )
        return redirect('core:mostrar-produtos')
    
class CadastrarUsuarioView(views.View):
    
    def get(self, request):
        form : CadastrarUsuarioForm = CadastrarUsuarioForm()
        
        context = {
            'form': form
        }
        return render(request, 'formularios/formulario_generico.html', context)
    
    def post(self, request):
        print(f"Request: {request.POST}")
        
        form = CadastrarUsuarioForm(request.POST)
        print(f"Form: {form}")
        
        if form.is_valid():
            form.save()
        return redirect('core:login')