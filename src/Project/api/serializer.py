from rest_framework import serializers
from .models import InfoAcademica, SocioEconomica, Estudiante
from .models import Egresados,EgreLaboral,EgreAcademica,EgreMotivacion

class SocioEconomicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocioEconomica
        fields = '__all__'

class InfoAcademicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfoAcademica
        fields = '__all__'

class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiante
        fields = '__all__'
        depth = 1

class EstudianteAgrupadoSerializer(serializers.Serializer):
    socioeconomica = SocioEconomicaSerializer()
    infoacademica = InfoAcademicaSerializer()
    datosEstudiante = EstudianteSerializer()

    def to_representation(self, instance):
        data = {
            'datasPers': EstudianteSerializer(instance).data,
            'datasSoci': SocioEconomicaSerializer(instance.socioeconomica).data,
            'datasAcad': InfoAcademicaSerializer(instance.infoacademica).data
        }
        return data


##EGRESADOS
class InfoAcademicaEgresadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = EgreAcademica
        fields = '__all__'

class LaboralEgresadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = EgreLaboral
        fields = '__all__'

class MotivacionEgresadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = EgreMotivacion
        fields = '__all__'

class EgresadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Egresados
        fields = '__all__'
        depth = 1

class EgresadosAgrupadoSerializer(serializers.Serializer):
    egresados = EgresadosSerializer()
    academica = InfoAcademicaEgresadosSerializer()
    laboral = LaboralEgresadosSerializer()
    motivacion = MotivacionEgresadosSerializer()

    def to_representation(self, instance):
        data = {
            'datasPers': EgresadosSerializer(instance).data,
            'datasAcad': InfoAcademicaEgresadosSerializer(instance.info_academica).data,
            'datasLab': LaboralEgresadosSerializer(instance.info_laboral).data,
            'datasMot': MotivacionEgresadosSerializer(instance.info_motivacion).data
        }
        return data


    
