
class Produit:
    def __init__(self, nom, prix, lien, vendeur="Amazon"):
        self.nom = nom
        self.prix = prix
        self.lien = lien
        self.vendeur = vendeur

    def __str__(self):
        return (
            f"Nom : {self.nom}\n"
            f"Prix : {self.prix}\n"
            f"Lien : {self.lien}\n"
            f"Vendeur : {self.vendeur}"
        )