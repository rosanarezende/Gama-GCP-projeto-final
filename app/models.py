from django.db import models

class Empresas(models.Model):
    nome = models.CharField(max_length=150)
    cnpj = models.CharField(max_length=14)
    email = models.EmailField(max_length=254)
    telefone = models.CharField(max_length=100)
    descricao = models.TextField(max_length=1024*2)
    cep = models.CharField(max_length=50)
    endereco = models.CharField(max_length=200)

class Categorias(models.Model):
    nome = models.CharField(max_length=100)

class Produtos(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=1000)
    qtde_estoque = models.IntegerField()
    preco = models.DecimalField(max_digits=9, decimal_places=2)
    empresa = models.ForeignKey(Empresas, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)