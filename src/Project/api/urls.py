from django.urls import path
from . import views
#from .views import CursoListView, homelist, registrar_curso, eliminar_curso, change_curso, edicion_curso
from .views import EstdListView, registrar_Estudiante, consultastd, consultas_p, eliminar_std, edicion_std , change_std
urlpatterns = [
    path('change/', change_std),
    path('edicionstd/<int:id>', edicion_std),
    #path('grafico/', CursoListView.as_view(), name='fp'),
    path('consultas_p/',views.consultas_p),
    path('consultastd/',consultastd,name='Consultas'),
    path('get_chart/', views.get_chart, name='get_chart'),
    path('home/', EstdListView.as_view(), name='Home'),
    path('registrarCurso/', registrar_Estudiante),
    path('eliminacionstd/<int:id>', eliminar_std)
]