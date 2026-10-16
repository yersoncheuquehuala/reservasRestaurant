from django.contrib import admin

# Register your models here.
from .models import Rol
from .models import Usuario
from .models import Restaurante
from .models import Mesa
from .models import Reserva
from .models import ReservaMesa
from .models import HistorialEstadoReserva
from .models import SituacionExcepcional

admin.site.register(Rol)
admin.site.register(Usuario)
admin.site.register(Restaurante)
admin.site.register(Mesa)
admin.site.register(Reserva)
admin.site.register(ReservaMesa)
admin.site.register(HistorialEstadoReserva)
admin.site.register(SituacionExcepcional)