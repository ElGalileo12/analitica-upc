from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from .models import Curso
from django.views.generic import ListView
from random import randrange
# Create your views here.


class CursoListView(ListView):
    model = Curso
    template_name = 'fp.html'

    def get_queryset(self):
        # return Curso.objects.filter(creditos__lte=4)
        return Curso.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context


class homelist(ListView):
    model = Curso
    template_name = 'home.html'

    def get_queryset(self):
        # return Curso.objects.filter(creditos__lte=4)
        return Curso.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context
    
def registrar_curso(request):
   nombre = request.POST['txtNombre']
   creditos = request.POST['numCreditos']
   curso = Curso.objects.create(nombre=nombre, creditos=creditos)
   return redirect('/api/home')

def eliminar_curso(request,id):
    curso = Curso.objects.get(id=id)
    curso.delete()

    return redirect('/api/home')

def edicion_curso(request, id):
    curso = Curso.objects.get(id=id)
    data = {
        'curso': curso
    }
    return render(request, "edicion.html", data)

def change_curso(request):
   id= int(request.POST['id'])
   nombre = request.POST['txtNombre']
   creditos = request.POST['numCreditos']
   curso = Curso.objects.get(id=id)
   curso.nombre = nombre
   curso.creditos = creditos
   curso.save()
 
   return redirect('/api/home')

def get_chart(_request):
    cursos_listados = Curso.objects.all()
    nombres = []
    creditos = []

# Itera a través de las instancias y agrega los valores a los arrays
    for item in cursos_listados:
        nombres.append(item.nombre)
        creditos.append(item.creditos)
        
    colors = ['blue', 'orange', 'red', 'black', 'yellow', 'green', 'magenta', 'lightblue', 'purple', 'brown']
    random_color = colors[randrange(0, (len(colors)-1))]

    chart = {
        'backgroundColor': '#000000',
        'tooltip' : {
        'trigger': 'axis',
        'axisPointer': {
          'type': 'cross'
            },
        },
        'xAxis': {
            'type': 'category',
            'data': nombres,
            'axisLabel': {
                'interval': 0  
            },
        },
        'yAxis': {
            'type': 'value'
        },
        'series': [
            {
            'data': creditos,
            'type': 'bar',
            'itemStyle': {
                    'color': random_color
            },
            'showBackground': 'true',
            'backgroundStyle': {
                'color': 'rgba(180, 180, 180, 0.2)'
            }
            }
        ]    
    }

    return JsonResponse(chart)