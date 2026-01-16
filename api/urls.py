# api/urls.py
from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

router.register('dinosaure', views.DinosaurViewSet)
router.register('localisation', views.LocalisationViewSet)
router.register('periode', views.PeriodeViewSet)
router.register('alimentation', views.AlimentationViewSet)
router.register('categorie', views.CategoryViewSet)

urlpatterns = [
    path('', include(router.urls))
]