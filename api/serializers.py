#api/serializers.py

from rest_framework import serializers
from .models import Dinosaur, Localisation, Periode, Alimentation, Category

# Sérialiseur pour le modèle Dinosaur
# Le sérialiseur convertit les instances du modèle en formats JSON/XML et vice versa
class DinosaurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dinosaur
        fields = '__all__'
        # fields = ['id', 'name', 'photo']

# Sérialiseur pour le modèle Localisation
class LocalisationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Localisation
        fields = '__all__'

# Sérialiseur pour le modèle Periode
class PeriodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Periode
        fields = '__all__'

# Sérialiseur pour le modèle Alimentation
class AlimentationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alimentation
        fields = '__all__'
    
# Sérialiseur pour le modèle Category
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'