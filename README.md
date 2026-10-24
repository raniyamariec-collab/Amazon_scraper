Amazon Scraper — Produits informatiques
 
1. Présentation du projet
 
Amazon Scraper est une application Python conçue pour rechercher des produits informatiques sur Amazon, récupérer les informations disponibles et les enregistrer dans une base de données SQLite.
 
L'application permet également d'afficher les produits enregistrés et d'exporter les résultats au format CSV.
 
Remarque : Amazon peut limiter les accès automatisés. Dans ce cas, la récupération des produits peut échouer même si le site fonctionne normalement dans un navigateur.
 
2. Objectifs
 
- Rechercher des produits informatiques à partir d'un mot-clé.
- Extraire le nom, le prix et le lien des produits disponibles.
- Enregistrer les produits dans une base de données SQLite.
- Rechercher et afficher les produits enregistrés.
- Exporter les données au format CSV.
- Tester les principales fonctionnalités de l'application.
 
3. Technologies utilisées
 
- Python
- Selenium
- SQLite
- CSV
- unittest
 
4. Architecture du projet
 
Amazon_scraper/
├── app/
│   ├── controllers/
│   ├── models/
│   ├── scraper/
│   └── views/
├── data/
├── exports/
├── tests/
├── config.py
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
 
5. Installation
 
Prérequis
 
- Python installé
- Google Chrome installé
- Git (facultatif)
 
Installer les dépendances
 
Dans un terminal ouvert à la racine du projet, exécuter :
 
pip install -r requirements.txt
 
6. Exécution
 
Lancer l'application avec :
 
python main.py
 
Saisir ensuite le mot-clé du produit à rechercher et suivre les instructions affichées dans le terminal.
 
7. Stockage des données
 
Les produits enregistrés sont stockés dans une base de données SQLite.
 
Les exportations CSV sont enregistrées dans le dossier "exports/".
 
8. Tests
 
Pour lancer les tests automatisés :
 
python -m unittest discover -s tests -p "test_*.py" -v
 
Les tests couvrent notamment l'enregistrement des produits, leur recherche et l'exportation CSV.
 
9. Limites connues
 
Amazon peut afficher une page d'erreur ou limiter les requêtes automatisées. Lorsque cela se produit, l'application peut ne récupérer aucun produit. Les fonctionnalités de stockage, de recherche locale et d'exportation peuvent néanmoins être testées avec des données fictives.
 
10. Auteur
 
Projet réalisé dans le cadre d'un travail pratique en programmation Python.