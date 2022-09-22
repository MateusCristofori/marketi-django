from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('cadastrar/<str:tipo>', views.CadastrarView.as_view(), name="cadastrar"),
    path('mostrar-produtos', views.MostrarProdutos.as_view(), name='mostrar-produtos'),
    path('cadastrar-usuario', views.CadastrarUsuarioView.as_view(), name='cadastrar-usuario'),
    path('login', views.LoginView.as_view(), name='login'),
    path('perfil', views.PerfilView.as_view(), name='perfil'),
    path('logout', views.logout_view, name='logout'),
    path('deletar/<int:produto_id>', views.DeletarProdutoView.as_view(), name='deletar-produto')
]
