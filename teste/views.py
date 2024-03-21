from django.shortcuts import render, HttpResponse, get_object_or_404,redirect
from .models import Produto
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def home(resquest):  
    nomes  = ['p1', 'p2', 'p3']
    produtos = [Produto(nome=i) for i in nomes]  
 

    Produto.objects.bulk_create(produtos)

    print(produtos)
    return HttpResponse(produtos)


