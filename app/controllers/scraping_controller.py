
from app.scraper.driver import creer_driver
from app.scraper.amazon_scraper import rechercher_produits
from app.models.depot import Depot
from app.views.console_view import afficher_message
from app.views.export_view import exporter_csv


class ScrapingController:
    """Coordonne la recherche, l'enregistrement et l'exportation."""

    def __init__(self):
        self.depot = Depot()

    def lancer_recherche(self, mot_cle):
        """Recherche des produits et les enregistre dans la base."""
        driver = None

        try:
            driver = creer_driver()
            afficher_message("\nRecherche en cours sur Amazon...")

            produits = rechercher_produits(driver, mot_cle)

            if produits:
                self.depot.enregistrer_produits(produits)
                afficher_message(
                    f"{len(produits)} produit(s) récupéré(s)."
                )
                afficher_message("Enregistrement dans la base terminé.")
            else:
                afficher_message("Aucun produit récupéré.")

            return produits

        except Exception as erreur:
            afficher_message(f"Une erreur est survenue : {erreur}")
            return []

        finally:
            if driver is not None:
                driver.quit()

    def afficher_produits_enregistres(self):
        """Affiche les produits présents dans la base."""
        self.depot.afficher_produits()

    def exporter_produits(self, produits):
        """Exporte les produits dans un fichier CSV."""
        if not produits:
            afficher_message("Aucun produit à exporter.")
            return

        exporter_csv(produits)

