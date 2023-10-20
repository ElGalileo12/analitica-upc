from django.urls import path, include
from rest_framework import routers
from . import views
#from .views import CursoListView, homelist, registrar_curso, eliminar_curso, change_curso, edicion_curso
from .views import  registrar_Estudiante, change_std, dashboard

router = routers.DefaultRouter()
router.register(r'Estudiante', views.studentViewSet)
router.register(r'Egresados', views.EgresadoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    #ruta inscripción
    path('inscripcion/', views.registrar_Estudiante, name='crear_registro'),
    path('inscripcion_egresados/', views.registrar_Egresados, name='crear_registro_e'),
    path('change/', views.change_std, name='edita_registro'),
    path('change_egresados/', views.change_egre, name='edita_registro_e'),
    #rutas de graficas
    path('get_chart/', views.get_chart, name='get_chart'),
    path('get_chart_2/', views.get_chart_2, name='get_chart_2'),
    path('get_chart_3/', views.get_chart_3, name='get_chart_3'),
    path('get_chart_4/', views.get_chart_4, name='get_chart_4'),
    path('get_chart_5/', views.get_chart_5, name='get_chart_5'),
    #---------------------#
    path('grafico/', dashboard, name='fp'),

]