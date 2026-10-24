import sqlite3
from pathlib import Path
 
from app.controllers.scraping_controller import ScrapingController
from app.views.console_view import (
    afficher_banniere,
    demander_mot_cle,
    afficher_message,
    demander_confirmation,
)
 
BASE_DIR = Path(__file__).resolve().parent
DATABASE_PATH = BASE_DIR / "data" / "amazon.db"
 
 
def initialiser_base_de_donnees():
    """Crée la base de données et la table des produits."""
    DATABASE_PATH.parent.mkdir(parents=True, exist_ok=True)
 
    with sqlite3.connect(DATABASE_PATH) as connexion:
        connexion.execute("""
            CREATE TABLE IF NOT EXISTS produits (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nom TEXT NOT NULL,
                prix TEXT,
                lien TEXT NOT NULL UNIQUE,
                vendeur TEXT DEFAULT 'Amazon'
            )
        """)
 
 
def lancer_application():
    """Lance l'application Amazon Scraper."""
    initialiser_base_de_donnees()
 
    controller = ScrapingController()
 
    afficher_banniere()
 
    mot_cle = demander_mot_cle()
 
    if not mot_cle:
        afficher_message("Tu dois saisir un mot-clé.")
        return
 
    produits = controller.lancer_recherche(mot_cle)
 
    if demander_confirmation("Veux-tu afficher les produits enregistrés ?"):
        controller.afficher_produits_enregistres()
 
    # Inutile d'exporter si la recherche n'a rien donné (ex. page bloquée)
    if not produits:
        afficher_message("Aucun produit récupéré : export CSV ignoré.")
        return
 
    if demander_confirmation("Veux-tu exporter les produits récupérés en CSV ?"):
        controller.exporter_produits(produits)
 
 
if __name__ == "__main__":
    lancer_application()
 