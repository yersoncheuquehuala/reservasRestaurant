from django.shortcuts import render
from rest_framework import viewsets

from .models import Rol
from .models import Usuario
from .models import Restaurante
from .models import Mesa
from .models import Reserva
from .models import ReservaMesa
from .models import HistorialEstadoReserva
from .models import SituacionExcepcional

from .serializer import RolSerializer
from .serializer import UsuarioSerializer
from .serializer import RestauranteSerializer
from .serializer import MesaSerializer
from .serializer import ReservaSerializer
from .serializer import ReservaMesaSerializer
from .serializer import HistorialEstadoReservaSerializer
from .serializer import SituacionExcepcionalSerializer

def home_page_view(request):
    # Django automatically looks inside your app's 'templates' folder
    return render(request, 'home.html')

class RolViewSet(viewsets.ModelViewSet):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class RestauranteViewSet(viewsets.ModelViewSet):
    queryset = Restaurante.objects.all()
    serializer_class = RestauranteSerializer

class MesaViewSet(viewsets.ModelViewSet):
    queryset = Mesa.objects.all()
    serializer_class = MesaSerializer

class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

class ReservaMesaViewSet(viewsets.ModelViewSet):
    queryset = ReservaMesa.objects.all()
    serializer_class = ReservaMesaSerializer

class HistorialEstadoReservaViewSet(viewsets.ModelViewSet):
    queryset = HistorialEstadoReserva.objects.all()
    serializer_class = HistorialEstadoReservaSerializer

class SituacionExcepcionalViewSet(viewsets.ModelViewSet):
    queryset = SituacionExcepcional.objects.all()
    serializer_class = SituacionExcepcionalSerializer