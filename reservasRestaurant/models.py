from django.db import models
from django.db.models import CASCADE
from django.utils.timezone import now


class Rol(models.Model):
    nombre = models.CharField(max_length=50, null=False)
    descripcion = models.TextField(max_length=250, null=False)
    nivel_acceso = models.IntegerField(null=False)
    es_administrador = models.BooleanField(default=False)
    activo = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(auto_now=True)


class Usuario(models.Model):
    rol = models.ForeignKey(Rol, on_delete=CASCADE)
    nombre = models.CharField(max_length=100, null=False)
    apellidos = models.CharField(max_length=150, null=False)
    email = models.EmailField(null=False)
    telefono = models.CharField(max_length=20, null=False)
    password = models.CharField(max_length=128, null=False)
    calificacion_comportamiento = models.FloatField(default=5.0)
    total_inasistencias = models.IntegerField(default=0)
    ultimo_acceso = models.DateTimeField(default=now)
    activo = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(auto_now=True)


class Restaurante(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    direccion = models.CharField(max_length=250, null=False)
    telefono = models.CharField(max_length=20, null=False)
    email_contacto = models.EmailField(null=False)
    sitio_web = models.URLField(null=True)
    hora_apertura = models.TimeField(null=False)
    hora_cierre = models.TimeField(null=False)
    capacidad_total = models.IntegerField(null=False)
    tiempo_tolerancia_minutos = models.IntegerField(default=15)
    informacion_publica = models.TextField(max_length=500, null=False)
    politicas_internas_privadas = models.TextField(max_length=500, null=False)
    activo = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(auto_now=True)


class Mesa(models.Model):
    restaurante = models.ForeignKey(Restaurante, on_delete=CASCADE)
    codigo_mesa = models.CharField(max_length=25, null=False)
    numero_mesa = models.IntegerField(null=False)
    capacidad_personas = models.IntegerField(null=False)
    ubicacion = models.CharField(max_length=50, null=False)
    disponible = models.BooleanField(default=True)
    activo = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(auto_now=True)


class Reserva(models.Model):
    cliente = models.ForeignKey(Usuario, on_delete=CASCADE)
    restaurante = models.ForeignKey(Restaurante, on_delete=CASCADE)
    codigo_reserva = models.CharField(max_length=25, null=False)
    fecha_reserva = models.DateField(null=False)
    hora_inicio = models.TimeField(null=False)
    hora_fin = models.TimeField(null=False)
    cantidad_personas = models.IntegerField(null=False)
    estado = models.CharField(max_length=50, null=False)
    observaciones_publicas_cliente = models.TextField(max_length=300, null=True)
    notas_privadas_administrador = models.TextField(max_length=300, null=True)
    activo = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(auto_now=True)


class ReservaMesa(models.Model):
    reserva = models.ForeignKey(Reserva, on_delete=CASCADE)
    mesa = models.ForeignKey(Mesa, on_delete=CASCADE)
    activo = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(auto_now=True)


class HistorialEstadoReserva(models.Model):
    reserva = models.ForeignKey(Reserva, on_delete=CASCADE)
    usuario_responsable = models.ForeignKey(Usuario, on_delete=CASCADE)
    estado_anterior = models.CharField(max_length=50, null=False)
    estado_nuevo = models.CharField(max_length=50, null=False)
    motivo_cambio = models.TextField(max_length=300, null=False)
    fecha_evento = models.DateTimeField(default=now, null=False)
    es_visible_cliente = models.BooleanField(default=True)
    activo = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(auto_now=True)


class SituacionExcepcional(models.Model):
    restaurante = models.ForeignKey(Restaurante, on_delete=CASCADE)
    reserva = models.ForeignKey(Reserva, on_delete=CASCADE, null=True)
    usuario_registro = models.ForeignKey(Usuario, on_delete=CASCADE)
    tipo_situacion = models.CharField(max_length=50, null=False)
    fecha_suceso = models.DateField(null=False)
    hora_suceso = models.TimeField(null=False)
    descripcion_publica = models.TextField(max_length=300, null=True)
    detalle_privado_auditoria = models.TextField(max_length=500, null=False)
    afecta_disponibilidad = models.BooleanField(default=False)
    resuelto = models.BooleanField(default=False)
    activo = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(auto_now=True)