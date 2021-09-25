from django.forms import ModelForm
from app import models

class EmpresasForm(ModelForm):
  class Meta:
    model = models.Empresas
    fields = ['nome', 'cnpj', 'email', 'telefone', 'descricao', 'cep', 'endereco', 'logo']

class ProdutosForm(ModelForm):
  class Meta:
    model = models.Produtos
    fields = ['id_empresa', 'nome', 'qtde_estoque', 'preco', 'id_categoria', 'descricao', 'imagem_produto']

