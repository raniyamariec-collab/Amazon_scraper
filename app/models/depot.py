
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
DATABASE_PATH = BASE_DIR / "data" / "amazon.db"


class Depot:
    def __init__(self):
        self.produits = []

    def ajouter_produit(self, produit):
        self.produits.append(produit)

    def enregistrer_produit(self, produit):
        connexion = sqlite3.connect(DATABASE_PATH)

        try:
            curseur = connexion.cursor()

            curseur.execute(
                """
                INSERT OR IGNORE INTO produits (nom, prix, lien, vendeur)
                VALUES (?, ?, ?, ?)
                """,
                (
                    produit.nom,
                    produit.prix,
                    produit.lien,
                    produit.vendeur,
                ),
            )

            connexion.commit()

        finally:
            connexion.close()

    def enregistrer_produits(self, produits):
        for produit in produits:
            self.enregistrer_produit(produit)

    def afficher_produits(self):
        connexion = sqlite3.connect(DATABASE_PATH)

        try:
            curseur = connexion.cursor()
            curseur.execute(
                "SELECT id, nom, prix, lien, vendeur FROM produits"
            )

            resultats = curseur.fetchall()

            if not resultats:
                print("Aucun produit enregistré dans la base de données.")
                return

            for resultat in resultats:
                print(f"ID : {resultat[0]}")
                print(f"Nom : {resultat[1]}")
                print(f"Prix : {resultat[2]}")
                print(f"Lien : {resultat[3]}")
                print(f"Vendeur : {resultat[4]}")
                print("-" * 40)

        finally:
            connexion.close()

    def rechercher_produit(self, mot_cle):
        connexion = sqlite3.connect(DATABASE_PATH)

        try:
            curseur = connexion.cursor()

            curseur.execute(
                """
                SELECT id, nom, prix, lien, vendeur
                FROM produits
                WHERE nom LIKE ?
                """,
                (f"%{mot_cle}%",),
            )

            return curseur.fetchall()

        finally:
            connexion.close()

