from django.shortcuts import render, redirect
from django import views
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from ..forms import CadastrarProdutoForm, CadastrarUsuarioForm, LoginForm
from ..models import Produto


def home_view(request): return render(request, 'home.html')

class MostrarProdutos(views.View):
    def get(self, request):
        produtos = Produto.objects.all()
        
        context = {
            'produtos': produtos
        }
        return render(request, 'display/mostrar_produtos.html', context)
    
    
class LoginView(views.View):
    template_name = 'formularios/formulario_generico.html'
    
    def get(self, request):
        form = LoginForm()
        
        context = {
            'form': form
        }
        return render(request, self.template_name, context)
    
    def post(self, request):
        form = LoginForm(request.POST)
        
        if form.is_valid():
            clean_form = form.cleaned_data
            username = clean_form.get('username')
            password = clean_form.get('password')
            
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('core:perfil')
            
        context = {
            'form': form
        }
        return render(request, self.template_name, context)
    

class PerfilView(LoginRequiredMixin, views.View):
    login_url = 'core:login'
    
    def get(self, request):
        context = {
            'user': request.user
        }
        return render(request, 'usuario/perfil.html', context)

class DeletarProdutoView(views.View):
    
    def get(self, request, produto_id):
        produto: Produto = Produto.objects.get(pk = produto_id)
        produto.delete()
        return redirect('core:mostrar-produtos')

def logout_view(request):
    logout(request)
    return redirect('core:login')
    