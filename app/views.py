from django.shortcuts import render, redirect
from app import models, forms
from django.http import HttpResponseRedirect

def home(request):
    data = {}
    data['produtos'] = models.Produtos.objects.all()
    return render(request, "index.html",data)

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
        data = {
            "produtos": produtosdaEmpresa,
            "empresa": pk
        }
    return render(request,"empresa.html", data)

def irParaEditarEmpresa(request,pk):
    data = {}
    data['empresa'] = models.Empresas.objects.get(pk=pk)
    data['formularioEmpresa'] = forms.EmpresasForm(instance=data['empresa'])
    return render(request,"cadastro-empresa.html", data)   

def salvarEditarEmpresa(request,pk):
    data = {}
    data['empresa'] = models.Empresas.objects.get(pk=pk)
    formularioEmpresa = forms.EmpresasForm(request.POST or None,instance=data['empresa'])
    if formularioEmpresa.is_valid():
        formularioEmpresa.save()
        return HttpResponseRedirect ("/empresas/")

def deletarEmpresa(request,pk):
    empresa = models.Empresas.objects.get(pk=pk)
    empresa.delete()
    return HttpResponseRedirect ("/empresas/")      

def irParaCadastroProduto(request, pk):
    data = {
        "formularioProduto": forms.ProdutosForm(),
        "categoriasProduto": models.Categorias.objects.all().order_by('nome'),
        "empresa": pk
    }
    return render(request, "cadastro-produto.html", data)

def salvarCadastrarProduto(request, pk):
    empresa = models.Empresas.objects.get(pk=pk)
    formularioProduto = models.Produtos(
        empresa=empresa, 
        nome=request.POST.get('nome'), 
        qtde_estoque=request.POST.get('qtde_estoque'), 
        preco=request.POST.get('preco'), 
        categoria_id=request.POST.get('categoria'), 
        descricao=request.POST.get('descricao')
    )
    formularioProduto.save()
    return redirect('empresa', pk)

def irParaEditarProduto(request,empresapk, pk):
    data = {}
    data['categoriasProduto'] = models.Categorias.objects.all().order_by('nome')
    data['produto'] = models.Produtos.objects.get(pk=pk)
    data['formularioProduto'] = forms.ProdutosForm(instance=data['produto'])
    data['empresa'] = empresapk
    return render(request,"cadastro-produto.html", data)

def salvarEditarProduto(request,empresapk, pk):
    empresa = models.Empresas.objects.get(pk=empresapk)
    data = {}
    data['produto'] = models.Produtos.objects.get(pk=pk)
    produto = models.Produtos(
        empresa=empresa,
        empresa_id = empresapk,
        nome=request.POST.get('nome'),
        qtde_estoque=request.POST.get('qtde_estoque'),
        preco=request.POST.get('preco'),
        categoria_id=request.POST.get('categoria'),
        descricao=request.POST.get('descricao')
    )
    formularioProduto = forms.ProdutosForm(request.POST or None, instance=produto)
    if formularioProduto.is_valid():
        formularioProduto.save()
        return HttpResponseRedirect ("/empresa/" + str(empresapk))

    # formularioProduto.save(update_fields=['nome'])

#
# def salvarEditarEmpresa(request,pk):
#     data = {}
#     data['empresa'] = models.Empresas.objects.get(pk=pk)
#     formularioEmpresa = forms.EmpresasForm(request.POST or None,instance=data['empresa'])
#     if formularioEmpresa.is_valid():
#         formularioEmpresa.save()
#         return HttpResponseRedirect ("/empresas/")



def deletarProduto(request,pk):
    produto = models.Produtos.objects.get(pk=pk)
    produto.delete()
    return HttpResponseRedirect ("/empresas/")