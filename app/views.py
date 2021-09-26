from django.shortcuts import render
from app import models, forms
from django.http import HttpResponseRedirect

def home(request):
    return render(request, "index.html")

def listarEmpresas(request):
    data = {}
    buscarNome = request.GET.get('buscar-nome')
    if buscarNome:
        data['empresas'] = models.Empresas.objects.filter(nome__icontains = buscarNome)
    else: 
        data['empresas'] = models.Empresas.objects.all()
    return render(request,"empresas.html", data)

def irParaCadastroEmpresa(request):
    data = {}
    data['formularioEmpresa'] = forms.EmpresasForm()
    return render(request, "cadastro-empresa.html", data)

def salvarCadastrarEmpresa(request):
    formularioEmpresa = forms.EmpresasForm(request.POST or None)
    if formularioEmpresa.is_valid():
        formularioEmpresa.save()
        return HttpResponseRedirect("/empresas/")

def listarProdutosdaEmpresa(request,pk):
    data = {}
    buscarNome = request.GET.get('buscar-nome-produto')
    produtosdaEmpresa = models.Produtos.objects.filter(empresa_id = pk)
    if buscarNome:
        data['produtos'] = produtosdaEmpresa.filter(nome__icontains = buscarNome)
    else: 
        data['produtos'] = produtosdaEmpresa
    return render(request,"empresa.html", data)

def irParaCadastroProduto(request):
    data = {}
    data['formularioProduto'] = forms.ProdutosForm()
    return render(request, "cadastro-produto.html", data)

def salvarCadastrarProduto(request, pk):
    formularioProduto = forms.ProdutosForm(request.POST or None)
    if formularioProduto.is_valid():
        formularioProduto.save()
        return HttpResponseRedirect("/empresa/", pk)