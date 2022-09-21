from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('cadastrar-produto/<str:tipo_produto>', views.CadastrarProdutoView.as_view(), name="cadastrar-produto"),
    path('mostrar-produtos', views.MostrarProdutos.as_view(), name='mostrar-produtos'),
    path('cadastrar-usuario', views.CadastrarUsuarioView.as_view(), name='cadastrar-usuario'),
    path('login', views.LoginView.as_view(), name='login'),
    path('perfil', views.PerfilView.as_view(), name='perfil'),
    path('logout', views.logout_view, name='logout'),
]
