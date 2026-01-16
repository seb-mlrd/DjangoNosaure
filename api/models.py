from django.db import models

class Dinosaur(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nom")
    scientific_name = models.CharField(max_length=150, verbose_name="Nom scientifique")
    periode = models.ForeignKey('Periode', on_delete=models.CASCADE, related_name='dinosaurs', verbose_name="Période")
    alimentation = models.ForeignKey('Alimentation', on_delete=models.CASCADE, related_name='dinosaurs', verbose_name="Alimentation")
    localisation = models.ManyToManyField('Localisation', related_name='dinosaurs', verbose_name="Localisation")
    taille = models.FloatField(help_text="Taille en mètres", verbose_name="Taille")
    poid = models.FloatField(help_text="Poids en kilogrammes", verbose_name="Poids")
    image = models.ImageField(upload_to='dinosaurs/', null=True, blank=True, verbose_name="Image")
    category = models.ManyToManyField('Category', related_name='dinosaurs', blank=True, verbose_name="Catégorie")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")
    class Meta:
        verbose_name = "Dinosaure"
        verbose_name_plural = "Dinosaures"
        
    def __str__(self):
        return self.name

class Alimentation(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nom")

    class Meta:
        verbose_name = "Alimentation"
        verbose_name_plural = "Alimentations"
        
    def __str__(self):
        return self.name
    
class Localisation(models.Model):
    country = models.CharField(max_length=100, blank=True, null=True, verbose_name="Pays")
    continent = models.CharField(max_length=100, verbose_name="Continent")

    class Meta:
        verbose_name = "Localisation"
        verbose_name_plural = "Localisations"
    def __str__(self):
        return f"{self.country}, {self.continent}"

class Periode(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nom")
    start = models.IntegerField(help_text="Début de la période en millions d'années", blank=True, null=True)
    end = models.IntegerField(help_text="Fin de la période en millions d'années", blank=True, null=True)

    class Meta:
        verbose_name = "Période"
        verbose_name_plural = "Périodes"

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = "Catégorie"
        verbose_name_plural = "Catégories"
    def __str__(self):
        return self.name
