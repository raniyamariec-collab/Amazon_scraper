import unittest
import csv
from pathlib import Path

from app.models.produit import Produit
from app.views.export_view import exporter_csv

class TestExport(unittest.TestCase):

```
def test_exporter_csv(self):
    produits = [
        Produit("Clavier numerique", "5 000 FCFA", "https://example.com/clavier"),
        Produit("Souris sans fil", "3 000 FCFA", "https://example.com/souris")
    ]

    exporter_csv(produits, "test_produits.csv")

    fichier = Path("exports") / "test_produits.csv"

    self.assertTrue(fichier.exists())

    with fichier.open("r", encoding="utf-8-sig", newline="") as csvfile:
        lignes = list(csv.reader(csvfile))

    self.assertGreaterEqual(len(lignes), 3)
    self.assertTrue(any("Clavier numerique" in cellule for cellule in lignes[1]))
    self.assertTrue(any("Souris sans fil" in cellule for cellule in lignes[2]))
```

if **name** == "**main**":
unittest.main()
