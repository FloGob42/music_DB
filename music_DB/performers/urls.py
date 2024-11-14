from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# Enregistrement du FilmViewSet dans le routeur
router.register(r'', views.PerformerViewSet)

urlpatterns = [
    # Inclusion des URLs générées par le routeur pour l'application 'film'
    path('', include(router.urls))
]
