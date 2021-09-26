from django.forms import ModelForm
from app import models

class EmpresasForm(ModelForm):
  class Meta:
    model = models.Empresas
    fields = ['nome', 'cnpj', 'email', 'telefone', 'descricao', 'cep', 'endereco']

class ProdutosForm(ModelForm):
  class Meta:
    model = models.Produtos
    fields = ['empresa', 'nome', 'qtde_estoque', 'preco', 'categoria', 'descricao']

