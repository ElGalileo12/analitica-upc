from rest_framework import serializers
from .models import Estudiante, SocioEconomica, InfoAcademica

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

