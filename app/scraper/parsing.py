from selenium.webdriver.common.by import By
from app.models.produit import Produit
 
 
def _extraire_titre(carte):
    """Le titre est dans le h2 (structure actuelle d'Amazon)."""
    h2 = carte.find_element(By.CSS_SELECTOR, "h2")
    titre = (h2.get_attribute("textContent") or "").strip()
    if not titre:
        titre = (h2.get_attribute("aria-label") or "").strip()
    return titre
 
 
def _extraire_lien(carte):
    """Construit un lien propre à partir de l'ASIN, sinon utilise le href."""
    asin = (carte.get_attribute("data-asin") or "").strip()
    if asin:
        return f"https://www.amazon.com/dp/{asin}"
 
    # Le lien englobe le h2 (nouveau) ou se trouve dedans (ancien)
    for selecteur in ("h2 a", "a.a-link-normal.s-no-outline"):
        try:
            return carte.find_element(By.CSS_SELECTOR, selecteur).get_attribute("href")
        except Exception:
            continue
 
    return carte.find_element(By.XPATH, ".//h2/ancestor::a").get_attribute("href")
 
 
def _extraire_prix(carte):
    """Le prix est masqué (a-offscreen) : .text renvoie vide, il faut textContent."""
    try:
        element = carte.find_element(By.CSS_SELECTOR, ".a-price .a-offscreen")
        prix = (element.get_attribute("textContent") or "").strip()
        return prix or "Prix indisponible"
    except Exception:
        return "Prix indisponible"
 
 
def analyser_produits(driver):
    """Analyse les résultats Amazon et affiche des informations de diagnostic."""
    produits = []
 
    cartes = driver.find_elements(
        By.CSS_SELECTOR,
        '[data-component-type="s-search-result"]'
    )
 
    print(f"Cartes de résultats trouvées : {len(cartes)}")
 
    for numero, carte in enumerate(cartes, start=1):
        try:
            titre = _extraire_titre(carte)
            lien = _extraire_lien(carte)
            prix = _extraire_prix(carte)
 
            if titre and lien:
                produits.append(Produit(nom=titre, prix=prix, lien=lien))
            else:
                print(f"Carte {numero} ignorée : titre ou lien vide.")
 
        except Exception as erreur:
            print(f"Carte {numero} ignorée : {erreur}")
 
    print(f"Produits extraits : {len(produits)}")
    return produits
 