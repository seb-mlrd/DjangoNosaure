# 🦖 DjangoNosaur - Encyclopédie des Dinosaures

**Auteur:** Sébastien Maillard  
**Date:** Janvier 2026

## 📋 Description

DjangoNosaur est une application web complète permettant de gérer une encyclopédie de dinosaures. Elle combine un backend Django avec API REST et un frontend Vue.js moderne.

**Fonctionnalités principales:**
- 📊 Gestion complète des dinosaures (CRUD)
- 🦕 Relations complexes (périodes, alimentations, localisations, catégories)
- 📈 Statistiques visuelles avec graphiques
- 📄 Export PDF et CSV
- 🎨 Interface admin personnalisée
- 🔄 API REST complète

---

## 🗄️ Structure de la Base de Données

### Tables principales

#### **Dinosaure**
- `id` (PK)
- `name` - Nom du dinosaure
- `scientific_name` - Nom scientifique
- `taille` - Taille en mètres (float)
- `poid` - Poids en kilogrammes (int)
- `image` - Image du dinosaure (optionnel)
- `created_at` - Date de création
- `periode` (FK) - Lien vers Période
- `alimentation` (FK) - Lien vers Alimentation
- `localisation` (M2M) - Localisations multiples
- `category` (M2M) - Catégories multiples

#### **Alimentation**
- `id` (PK)
- `name` - Nom (ex: Herbivore, Carnivore, Omnivore)

#### **Localisation**
- `id` (PK)
- `country` - Pays
- `continent` - Continent

#### **Periode**
- `id` (PK)
- `name` - Nom de la période (ex: Trias, Jurassique, Crétacé)
- `start` - Date de début (millions d'années)
- `end` - Date de fin (millions d'années)

#### **Category**
- `id` (PK)
- `name` - Nom de la catégorie (ex: Carnosaures, Sauropodes)

---

## 🚀 Installation et Configuration

### Prérequis

- **Python** 3.13+
- **Node.js** 20.19+ ou 22.12+
- **pip** (gestionnaire de paquets Python)
- **npm** (gestionnaire de paquets Node.js)
- Base de données **Oracle** (ou SQLite pour le développement)

### 1️⃣ Cloner le projet

```bash
git clone <url-du-repo>
cd djangoNosaur
```

### 2️⃣ Configuration du Backend Django

#### Créer l'environnement virtuel

```bash
python3 -m venv .venv
source .venv/bin/activate  # Sur macOS/Linux
# ou
.venv\Scripts\activate  # Sur Windows
```

#### Installer les dépendances Python

```bash
pip install -r requirements.txt
```

#### Créer le fichier `.env`

À la racine du projet, créer un fichier `.env` avec:

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
DB_ENGINE=django.db.backends.oracle
DB_HOST=localhost
DB_PORT=1521
DB_NAME=XE
DB_USER=votre_utilisateur
DB_PASSWORD=votre_mot_de_passe
```

#### Appliquer les migrations

```bash
python manage.py migrate
```

#### Créer un super utilisateur

```bash
python manage.py createsuperuser
```

Remplissez les informations demandées (email, mot de passe, etc.)

#### Générer des données aléatoires (optionnel)

```bash
python manage.py seed_dinosaurs --count 20
```

Cela créera 20 dinosaures aléatoires avec les données de base.

#### Lancer le serveur Django

```bash
python manage.py runserver
# ou avec make:
make run
```

Le serveur sera accessible à `http://127.0.0.1:8000`

### 3️⃣ Configuration du Frontend Vue.js

#### Accéder au dossier frontend

```bash
cd frontend
```

#### Installer les dépendances Node.js

```bash
npm install
```

#### Lancer le serveur de développement

```bash
npm run dev
```

Le frontend sera accessible à `http://localhost:5174`

---

## 📚 Utilisation

### Interface Admin Django

1. Allez sur `http://127.0.0.1:8000/admin/`
2. Connectez-vous avec votre super utilisateur
3. Gérez les dinosaures, périodes, alimentations, etc.

**Actions disponibles:**
- ✅ Générer 10 dinosaures aléatoires
- 📄 Exporter en PDF
- 📊 Exporter en CSV
- 📈 Voir les statistiques d'alimentation

### API REST

L'API est disponible à `http://127.0.0.1:8000/api/v1/`

**Endpoints principaux:**
- `GET /api/v1/dinosaure/` - Liste des dinosaures
- `GET /api/v1/dinosaure/{id}/` - Détail d'un dinosaure
- `POST /api/v1/dinosaure/` - Créer un dinosaure
- `PUT /api/v1/dinosaure/{id}/` - Modifier un dinosaure
- `DELETE /api/v1/dinosaure/{id}/` - Supprimer un dinosaure

**Autres endpoints:**
- `/api/v1/periode/` - Gestion des périodes
- `/api/v1/alimentation/` - Gestion des alimentations
- `/api/v1/localisation/` - Gestion des localisations
- `/api/v1/categorie/` - Gestion des catégories

### Frontend Vue.js

Accédez à `http://localhost:5174` pour voir la liste des dinosaures avec:
- Affichage complet des informations
- Recherche et filtrage
- Interface responsive

---

## 🛠️ Commandes Utiles

```bash
# Backend - Django
make run              # Lancer le serveur
make migrate          # Appliquer les migrations
make migration        # Créer les migrations
make user             # Créer un super utilisateur
make shell            # Ouvrir le shell Django
make test             # Lancer les tests
make freeze           # Mettre à jour requirements.txt

# Frontend - Vue.js
npm run dev           # Lancer le serveur de développement
npm run build         # Compiler pour la production
npm run lint          # Vérifier le code (ESLint)
npm run format        # Formater le code (Prettier)
```

---

## 🔐 CORS et Sécurité

Pour que le frontend Vue.js puisse communiquer avec l'API Django:

✅ **CORS est activé** dans les settings Django
✅ **Hôtes locaux** sont autorisés
✅ **Développement local** uniquement

Pour la production, mettre à jour les `ALLOWED_HOSTS` et `CORS_ALLOWED_ORIGINS` dans `config/settings.py`.

---

## 📁 Structure du Projet

```
djangoNosaur/
├── api/                           # Application Django principale
│   ├── admin.py                   # Configuration admin personnalisée
│   ├── models.py                  # Modèles de données
│   ├── serializers.py             # Sérialiseurs DRF
│   ├── views.py                   # Vues API
│   ├── urls.py                    # Routes API
│   └── management/commands/
│       └── seed_dinosaurs.py      # Commande de génération de données
│
├── config/                        # Configuration Django
│   ├── settings.py                # Paramètres globaux
│   ├── urls.py                    # Routeur principal
│   └── wsgi.py                    # WSGI (production)
│
├── frontend/                      # Application Vue.js
│   ├── src/
│   │   ├── components/            # Composants Vue
│   │   ├── views/                 # Pages Vue
│   │   ├── composables/           # Composables réutilisables
│   │   ├── services/              # Services API
│   │   └── App.vue                # Composant racine
│   └── package.json               # Dépendances Node.js
│
├── templates/                     # Templates HTML
│   └── admin/                     # Templates admin personnalisés
│
├── manage.py                      # Gestionnaire Django
├── requirements.txt               # Dépendances Python
├── Makefile                       # Commandes automatisées
└── README.md                      # Ce fichier
```

---

## 🐛 Dépannage

### Erreur: "TemplateDoesNotExist"
- Vérifier que `DIRS` est configuré dans `settings.py`
- S'assurer que le dossier `templates/` existe

### Erreur: "ModuleNotFoundError"
- Vérifier que l'environnement virtuel est activé
- Réinstaller les dépendances: `pip install -r requirements.txt`

### Erreur CORS
- Vérifier les `CORS_ALLOWED_ORIGINS` dans `settings.py`
- S'assurer que le frontend accède à `http://127.0.0.1:8000`

### Erreur de Base de Données
- Vérifier la configuration `.env`
- S'assurer qu'Oracle/la base de données est accessible
- Lancer les migrations: `python manage.py migrate`

---

## 📝 Notes de Développement

- **Backend:** Django 6.0.1 + Django REST Framework
- **Frontend:** Vue.js 3 + Vite
- **Styling:** CSS personnalisé (thème dinosaure)
- **Base de données:** Oracle ou SQLite (développement)

---

## 📄 Licence

Ce projet est créé à des fins pédagogiques.

**Auteur:** Sébastien Maillard  
**Établissement:** Digital Campus - B3DEV  
**Date:** Janvier 2026


