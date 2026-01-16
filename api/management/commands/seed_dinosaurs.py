from django.core.management.base import BaseCommand
from django.db.models import Q
from api.models import Dinosaur, Periode, Alimentation, Localisation, Category
import random
import string

class Command(BaseCommand):
    help = 'Génère des données aléatoires pour les dinosaures'

    def add_arguments(self, parser):
        parser.add_argument(
            '--count',
            type=int,
            default=10,
            help='Nombre de dinosaures à générer (par défaut: 10)',
        )

    def handle(self, *args, **options):
        count = options['count']
        
        # Données de base
        dinosaur_names = [
            'Tyrannosaure', 'Tricératops', 'Vélociraptor', 'Stégosaure', 'Ankylosaure',
            'Parasaurolophus', 'Spinosaure', 'Carnotaure', 'Iguanodon', 'Compsognathus',
            'Brachiosaurus', 'Diplodocus', 'Allosaurus', 'Ceratosaurus', 'Gallimimus',
            'Deinonychus', 'Triceratops', 'Edmontosaurus', 'Hesperosaurus', 'Dracorex'
        ]
        
        scientific_names = [
            'Tyrannosaurus rex', 'Triceratops horridus', 'Velociraptor mongoliensis',
            'Stegosaurus stenops', 'Ankylosaurus magniventris', 'Parasaurolophus walkeri',
            'Spinosaurus aegyptiacus', 'Carnotaurus sastrei', 'Iguanodon bernissartensis',
            'Compsognathus longipes', 'Brachiosaurus brancai', 'Diplodocus carnegiei',
            'Allosaurus fragilis', 'Ceratosaurus nasicornis', 'Gallimimus bullatus',
            'Deinonychus antirrhopus', 'Triceratops prorsus', 'Edmontosaurus regalis',
            'Hesperosaurus mjosi', 'Dracorex hogwartsia'
        ]
        
        locations = [
            ('États-Unis', 'Amérique du Nord'),
            ('Canada', 'Amérique du Nord'),
            ('Chine', 'Asie'),
            ('Argentine', 'Amérique du Sud'),
            ('Mongolie', 'Asie'),
            ('Allemagne', 'Europe'),
            ('Australie', 'Océanie'),
            ('Afrique du Sud', 'Afrique'),
            ('Brésil', 'Amérique du Sud'),
            ('Japon', 'Asie'),
        ]
        
        # Créer les données de base si elles n'existent pas
        self.stdout.write('Création des données de base...')
        
        # Périodes
        periods = ['Trias', 'Jurassique', 'Crétacé']
        periode_objs = []
        for period in periods:
            p, _ = Periode.objects.get_or_create(
                name=period,
                defaults={'start': random.randint(-300, -65), 'end': random.randint(-300, -65)}
            )
            periode_objs.append(p)
        self.stdout.write(f'✓ Périodes créées: {len(periode_objs)}')
        
        # Alimentations
        alimentations = ['Herbivore', 'Carnivore', 'Omnivore']
        alimentation_objs = []
        for alim in alimentations:
            a, _ = Alimentation.objects.get_or_create(name=alim)
            alimentation_objs.append(a)
        self.stdout.write(f'✓ Alimentations créées: {len(alimentation_objs)}')
        
        # Localisations
        localisation_objs = []
        for country, continent in locations:
            l, _ = Localisation.objects.get_or_create(
                country=country,
                continent=continent
            )
            localisation_objs.append(l)
        self.stdout.write(f'✓ Localisations créées: {len(localisation_objs)}')
        
        # Catégories
        categories = ['Carnosaures', 'Cératopsiens', 'Ornithopodes', 'Sauropodes', 'Théropodes', 'Ankylosaures']
        category_objs = []
        for cat in categories:
            c, _ = Category.objects.get_or_create(name=cat)
            category_objs.append(c)
        self.stdout.write(f'✓ Catégories créées: {len(category_objs)}')
        
        # Générer les dinosaures
        self.stdout.write(f'\nGénération de {count} dinosaures aléatoires...')
        created_count = 0
        
        for i in range(count):
            try:
                name = f"{random.choice(dinosaur_names)}"
                
                # Vérifier si le dinosaure existe déjà
                if Dinosaur.objects.filter(name=name).exists():
                    continue
                
                dino = Dinosaur.objects.create(
                    name=name,
                    scientific_name=random.choice(scientific_names),
                    taille=round(random.uniform(2, 50), 2),
                    poid=random.randint(100, 100000),
                    periode=random.choice(periode_objs),
                    alimentation=random.choice(alimentation_objs),
                )
                
                # Ajouter des localisations aléatoires
                dino.localisation.set(random.sample(localisation_objs, k=random.randint(1, 3)))
                
                # Ajouter des catégories aléatoires
                dino.category.set(random.sample(category_objs, k=random.randint(1, 3)))
                
                created_count += 1
                self.stdout.write(f'  ✓ Créé: {dino.name}')
                
            except Exception as e:
                self.stdout.write(self.style.WARNING(f'  ✗ Erreur: {e}'))
        
        self.stdout.write(
            self.style.SUCCESS(f'\n✅ Succès! {created_count} dinosaures générés!')
        )
