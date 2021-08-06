import json
from django.shortcuts import render
from django.http.response import JsonResponse, HttpResponse
from apps.web.models import (Programa, Capitulos, Productora, Principal)


def home(request):
    tipo_pagina = 'web'
    programas = Programa.objects.all()
    video = Principal.objects.all().order_by('order_video')
    for programa in programas:
        capitulos = programa.programa.all
        print("titulo", capitulos)
            
    return render(request, "index.html", locals())


def capitulo_detalle(request, slug):
    capitulo_detallado = Capitulos.objects.select_related("programa").get(slug=slug)
    
    programa = Programa.objects.get(nombre=capitulo_detallado.programa)
    capitulos = programa.programa.all()
    programas = Programa.objects.all()
    urls = Capitulos.objects.filter(slug=slug)
    return render(request, 'capitulo_template.html', locals())



def buscador(request):
    if request.is_ajax() and request.method == 'POST':
        data = json.loads(request.read().decode('utf-8'))
        titulo = data['busqueda']
        
        if titulo:
        	capitulos = Capitulos.objects.filter(titulo__icontains=titulo)
        	print('capitulos', capitulos)
        	items_list = []
        	for item in capitulos:
        		titulo = item.titulo
        		image_url = item.imagen_principal.url
        		numero_capitulo = item.numero_capitulo
        		slug = item.slug
        		capitulo = {'titulo': titulo, 'image_url': image_url, 'numero_capitulo': numero_capitulo, 'slug': slug}
        		items_list.append(capitulo)
        		print('items_list', items_list)
        return JsonResponse({'items_list': items_list})

def app(request):
    response = HttpResponse("", status=302)
    response['Location'] = "https://play.google.com/store/apps/details?id=com.teveempresa.harolcalzada"
    return response


def app_ios(request):
    response = HttpResponse("", status=302)
    response['Location'] = "https://apps.apple.com/pe/app/teve-empresa/id1523399809"
    return response