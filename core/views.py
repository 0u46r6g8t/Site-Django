from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http.response import HttpResponse, Http404
from .forms import ProdutoModelForm
from .models import Produtos, Attack
import os
# Create your views here.

def page(request):

    return render(request, 'main.html')

def index(request):
    products = Produtos.objects.all()

    return render(request, 'load.html', {'products':products})

def add(request):

    if(request.method == "POST"):
        form = ProdutoModelForm(request.POST, request.FILES)
        if(form.is_valid()):
            form.save()
            return redirect( '/add' )
    else:
        form = ProdutoModelForm()

    context = {
        'form': form
    }

    return render(request, 'index.html', context)

def delete_arq(request, id_request):

    try:
       product = Produtos.objects.get(id=id_request)
       arq = "/media/{}".format(product.photo)
       product.delete()
       print(arq)
       os.remove(arq)
    except Exception:
        return Http404()
    finally:
        return redirect('/load/')

def pageAttack(request):

    attacks = Attack.objects.all()

    attack = {'attacks':attacks}

    return render(request, 'Attack.html', attack)