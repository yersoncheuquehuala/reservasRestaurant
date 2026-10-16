from rest_framework import serializers

from .models import Rol
from .models import Usuario
from .models import Restaurante
from .models import Mesa
from .models import Reserva
from .models import ReservaMesa
from .models import HistorialEstadoReserva
from .models import SituacionExcepcional

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = ('__all__')


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = (
            'rol',
            'nombre',
            'apellidos',
            'email',
            'telefono',
            'calificacion_comportamiento',
            'total_inasistencias',
            'activo'
        )
        # deje fuera password


class RestauranteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurante
        fields = (
            'nombre',
            'direccion',
            'telefono',
            'email_contacto',
            'sitio_web',
            'hora_apertura',
            'hora_cierre',
            'capacidad_total',
            'tiempo_tolerancia_minutos',
            'informacion_publica',
            'activo'
        )
        # 'politicas_internas_privadas'


class MesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mesa
        fields = ('__all__')


class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = ('__all__')


class ReservaMesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReservaMesa
        fields = ('reserva', 'mesa', 'activo')
        # fechas


class HistorialEstadoReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistorialEstadoReserva
        fields = ('__all__')


class SituacionExcepcionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = SituacionExcepcional
        fields = (
            'restaurante',
            'reserva',
            'usuario_registro',
            'tipo_situacion',
            'fecha_suceso',
            'hora_suceso',
            'descripcion_publica',
            'afecta_disponibilidad',
            'resuelto'
        )
        # detalle_privado_auditoria