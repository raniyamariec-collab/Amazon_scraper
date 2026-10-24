
import csv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
DOSSIER_EXPORT = BASE_DIR / "exports"


def exporter_csv(produits, nom_fichier="produits_amazon.csv"):
    """Exporte une liste de produits dans un fichier CSV."""
    DOSSIER_EXPORT.mkdir(parents=True, exist_ok=True)
    chemin_fichier = DOSSIER_EXPORT / nom_fichier

    with open(
        chemin_fichier,
        mode="w",
        newline="",
        encoding="utf-8-sig"
    ) as fichier:
        champs = ["nom", "prix", "lien", "vendeur"]
        writer = csv.DictWriter(fichier, fieldnames=champs)
        writer.writeheader()

        for produit in produits:
            writer.writerow({
                "nom": produit.nom,
                "prix": produit.prix,
                "lien": produit.lien,
                "vendeur": produit.vendeur
            })

    print(f"Export CSV réussi : {chemin_fichier}")

