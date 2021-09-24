from django.db import models
from localflavor.br.models import BRCNPJField, BRPostalCodeField
from phonenumber_field.modelfields import PhoneNumberField

'''
Modelagem das tabelas do banco de dados
'''

class Empresas(models.Model):
    nome = models.CharField(max_length=150)
    cnpj = BRCNPJField()
    email = models.EmailField(max_length=254)
    telefone = PhoneNumberField()
    descricao = models.CharField(max_length=200)
    cep = BRPostalCodeField()
    endereco = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='imagens/logos')

class Categorias(models.Model):
    nome = models.CharField(max_length=100)

class Produtos(models.Model):
    id_empresa = models.ForeignKey(Empresas, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    qtde_estoque = models.IntegerField()
    preco = models.DecimalField(max_digits=9, decimal_places=2)
    id_categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=1000)
    imagem_produto = models.ImageField(upload_to='imagens/produtos')
