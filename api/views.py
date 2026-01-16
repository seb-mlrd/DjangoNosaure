from django.shortcuts import render

from rest_framework import viewsets, filters
from .serializers import DinosaurSerializer, LocalisationSerializer, PeriodeSerializer, AlimentationSerializer, CategorySerializer
from .models import Dinosaur, Localisation, Periode, Alimentation, Category

class DinosaurViewSet(viewsets.ModelViewSet):
    queryset = Dinosaur.objects.all().order_by('name') # Trier les dinosaures par nom
    serializer_class = DinosaurSerializer # Utiliser le sérialiseur DinosaurSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter] # Activer la recherche
    search_fields = ['name'] # Champs de recherche : nom et type
    ordering_fields = ['id', 'name', 'taille', 'age'] # Champs pour le tri

class LocalisationViewSet(viewsets.ModelViewSet):
    queryset = Localisation.objects.all().order_by('continent')
    serializer_class = LocalisationSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['continent']
    ordering_fields = ['id', 'continent']

class PeriodeViewSet(viewsets.ModelViewSet):
    queryset = Periode.objects.all().order_by('name')
    serializer_class = PeriodeSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['id', 'name']
    
class AlimentationViewSet(viewsets.ModelViewSet):
    queryset = Alimentation.objects.all().order_by('name')
    serializer_class = AlimentationSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['id', 'name']

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['id', 'name']