from django.contrib import admin
from .models import InfoAcademica, SocioEconomica, Estudiante

#admin.site.register(Estudiante)
#admin.site.register(SocioEconomica)
#admin.site.register(InfoAcademica)
# Register your models here.
@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
   list_display = ('ID_DOCUMENTO', 'ID_NOMBRE')
    # ordering = ('creditos', 'nombre')
    # search_fields = ('nombre', 'creditos')
    # list_editable = ('nombre','creditos')
    # list_display_links = ('nombre',)
    # list_filter = ('creditos',)
    # list_per_page = 3 # Paginación
    # exclude = ('creditos',)
def datos(self, obj):
    return obj.ID_NOMBRE.upper()

   # datos.short_description = "CURSO (MAYÚS)"
    #datos.empty_value_display = "???"
    #datos.admin_order_field = 'nombre'
    
    
@admin.register(InfoAcademica)
class AcademicoAdmin(admin.ModelAdmin):
   list_display = ('ID_ESTUDIANTE', 'ID_PROGR_ACTUAL','ID_UBICACION_SEMESTRE')
def datos(self, obj):
    return obj.ID_PROGR_ACTUAL.upper()  

@admin.register(SocioEconomica)
class SocioAdmin(admin.ModelAdmin):
   list_display = ('ID_ESTUDIANTE', 'ID_ESTRATO','ID_OCUPACION')
def datos(self, obj):
    return obj.ID_PROGR_ACTUAL.upper()  