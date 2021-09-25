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
    return render(request, "cadastro-empresa.html")

def salvarCadastrarEmpresa(request):
    formularioEmpresa = forms.EmpresasForm(request.POST or None)
    if formularioEmpresa.is_valid():
        formularioEmpresa.save()
        return HttpResponseRedirect("/")