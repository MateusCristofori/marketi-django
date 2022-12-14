from django.db import models

class Produto(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    lote = models.CharField(max_length=100)
    preco = models.FloatField(verbose_name="Preço")
    
    
class Monitor(Produto):
    tamanho = models.IntegerField()
    taxa_de_atualizacao = models.IntegerField()
    resolucao = models.CharField(max_length=15)
    tipo_de_tela = models.CharField(max_length=10)
    
    
class Computador(Produto):
    memoria_ram = models.IntegerField()
    armazenamento = models.IntegerField()
    sistema_operacional = models.CharField(max_length=50)
    
    
class Funcionario(models.Model):
    CARGO_CHOICES = (
        ('CAIXA', 'Caixa'),
        ('ESTOQUISTA', 'Estoquista'),
        ('GERENTE', 'Gerente'),
        ('TECNICO', 'Técnico')
    )

    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100, choices=CARGO_CHOICES)
    matricula = models.CharField(max_length=100)
    data_de_admissao = models.DateField()