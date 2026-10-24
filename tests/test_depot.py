import unittest

from app.models.produit import Produit
from app.models.depot import Depot
from main import initialiser_base_de_donnees


class TestDepot(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        initialiser_base_de_donnees()
        cls.depot = Depot()

    def test_enregistrer_un_produit(self):
        produit = Produit(
            "Produit test clavier",
            "5 000 FCFA",
            "https://example.com/test-clavier"
        )

        self.depot.enregistrer_produit(produit)

        resultat = self.depot.rechercher_produit(
            "Produit test clavier"
        )

        self.assertIsNotNone(resultat)

    def test_rechercher_un_produit(self):
        produit = Produit(
            "Produit test souris",
            "3 000 FCFA",
            "https://example.com/test-souris"
        )

        self.depot.enregistrer_produit(produit)

        resultat = self.depot.rechercher_produit(
            "Produit test souris"
        )

        self.assertIsNotNone(resultat)


if __name__ == "__main__":
    unittest.main()
