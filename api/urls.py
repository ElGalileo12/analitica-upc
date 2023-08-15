from django.urls import path
from . import views
from .views import CursoListView, homelist, registrar_curso, eliminar_curso, change_curso, edicion_curso

urlpatterns = [
    path('borrar/<int:id>', eliminar_curso),
    path('change/', change_curso),
    path('edicionCurso/<int:id>', edicion_curso),
    path('grafico/', CursoListView.as_view(), name='fp'),
    path('get_chart/', views.get_chart, name='get_chart'),
    path('home/', homelist.as_view(), name='Home'),
    path('registrarCurso/', registrar_curso),
    
    
]