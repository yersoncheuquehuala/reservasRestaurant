from django.urls import path,include
from rest_framework import routers
from reservasRestaurant import views

router = routers.DefaultRouter()

router.register(r'rol', views.RolViewSet)
router.register(r'usuario', views.UsuarioViewSet)
router.register(r'restaurante', views.RestauranteViewSet)
router.register(r'mesa', views.MesaViewSet)
router.register(r'reserva', views.ReservaViewSet)
router.register(r'reservamesa', views.ReservaMesaViewSet)
router.register(r'historialestadoreserva', views.HistorialEstadoReservaViewSet)
router.register(r'situacionexcepcional', views.SituacionExcepcionalViewSet)


urlpatterns = [
    path('', include(router.urls))
]