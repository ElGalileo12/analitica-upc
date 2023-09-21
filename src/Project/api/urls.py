from django.urls import path, include
from rest_framework import routers
from . import views
#from .views import CursoListView, homelist, registrar_curso, eliminar_curso, change_curso, edicion_curso
from .views import EstdListView, registrar_Estudiante, consultastd, consultas_p, eliminar_std, edicion_std , change_std,dashboard

router = routers.DefaultRouter()
router.register(r'Estudiante', views.studentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    #rutas de graficas
    path('get_chart/', views.get_chart, name='get_chart'),
    path('get_chart_2/', views.get_chart_2, name='get_chart_2'),
    path('get_chart_3/', views.get_chart_3, name='get_chart_3'),
    path('get_chart_4/', views.get_chart_4, name='get_chart_4'),
    path('get_chart_5/', views.get_chart_5, name='get_chart_5'),
    #---------------------#
    path('change/', change_std),
    path('edicionstd/<int:id>', edicion_std),
    path('grafico/', dashboard, name='fp'),
    path('consultas_p/',views.consultas_p),
    path('consultastd/',consultastd,name='Consultas'),
    path('home/', EstdListView.as_view(), name='Home'),
    path('registrarCurso/', registrar_Estudiante),
    path('eliminacionstd/<int:id>', eliminar_std)  
]