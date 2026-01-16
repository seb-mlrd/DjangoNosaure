#api/serializers.py

from rest_framework import serializers
from .models import Dinosaur, Localisation, Periode, Alimentation, Category

# Sérialiseurs simples pour les modèles de référence
class LocalisationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Localisation
        fields = '__all__'

class PeriodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Periode
        fields = '__all__'

class AlimentationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alimentation
        fields = '__all__'
    
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

# Sérialiseur pour le modèle Dinosaur avec objets imbriqués
class DinosaurSerializer(serializers.ModelSerializer):
    # Utiliser les serializers imbriqués pour retourner les objets complets
    periode = PeriodeSerializer(read_only=True)
    alimentation = AlimentationSerializer(read_only=True)
    localisation = LocalisationSerializer(many=True, read_only=True)
    category = CategorySerializer(many=True, read_only=True)
    
    # Champs pour l'écriture (accepter les IDs)
    periode_id = serializers.PrimaryKeyRelatedField(
        queryset=Periode.objects.all(), source='periode', write_only=True
    )
    alimentation_id = serializers.PrimaryKeyRelatedField(
        queryset=Alimentation.objects.all(), source='alimentation', write_only=True
    )
    localisation_ids = serializers.PrimaryKeyRelatedField(
        queryset=Localisation.objects.all(), source='localisation', write_only=True, many=True
    )
    category_ids = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source='category', write_only=True, many=True, required=False
    )
    
    class Meta:
        model = Dinosaur
        fields = [
            'id', 'name', 'scientific_name', 'taille', 'poid', 'image', 'created_at',
            'periode', 'periode_id',
            'alimentation', 'alimentation_id',
            'localisation', 'localisation_ids',
            'category', 'category_ids'
        ]
        read_only_fields = ['id', 'created_at']