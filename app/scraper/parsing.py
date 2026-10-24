
from selenium.webdriver.common.by import By
from app.models.produit import Produit


def analyser_produits(driver):
    """Analyse le HTML des résultats Amazon et récupère les produits."""
    produits = []

    cartes = driver.find_elements(
        By.CSS_SELECTOR,
        '[data-component-type="s-search-result"]'
    )

    for carte in cartes:
        try:
            titre = carte.find_element(
                By.CSS_SELECTOR, "h2 a span"
            ).text.strip()

            lien = carte.find_element(
                By.CSS_SELECTOR, "h2 a"
            ).get_attribute("href")

            try:
                prix = carte.find_element(
                    By.CSS_SELECTOR, ".a-price .a-offscreen"
                ).text.strip()
            except Exception:
                prix = "Prix indisponible"

            if titre and lien:
                produit = Produit(
                    nom=titre,
                    prix=prix,
                    lien=lien
                )
                produits.append(produit)

        except Exception:
            continue

    return produits

