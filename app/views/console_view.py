
def afficher_banniere():
    """Affiche le titre de l'application."""
    print("=" * 45)
    print("       AMAZON SCRAPER - PRODUITS IT")
    print("=" * 45)


def demander_mot_cle():
    """Demande à l'utilisateur le produit à rechercher."""
    mot_cle = input(
        "Quel produit informatique veux-tu rechercher ? "
    ).strip()
    return mot_cle


def afficher_message(message):
    """Affiche un message dans le terminal."""
    print(message)


def demander_confirmation(message):
    """Demande une réponse oui/non à l'utilisateur."""
    while True:
        reponse = input(f"{message} (o/n) : ").strip().lower()

        if reponse in ("o", "oui"):
            return True

        if reponse in ("n", "non"):
            return False

        print("Réponse invalide. Saisis o ou n.")

