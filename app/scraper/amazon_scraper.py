
from urllib.parse import quote_plus

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException

from app.scraper.parsing import analyser_produits


def rechercher_produits(driver, mot_cle):
    """Recherche des produits sur Amazon et analyse les résultats."""

    url = f"https://www.amazon.com/s?k={quote_plus(mot_cle)}"

    try:
        print("\nOuverture de la page Amazon...")
        driver.get(url)

        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, '[data-component-type="s-search-result"]')
            )
        )

        produits = analyser_produits(driver)

        print("Titre de la page :", driver.title)
        print("Nombre de produits détectés :", len(produits))

        if not produits:
            print("La page est accessible, mais aucun produit n'a été extrait.")

        return produits

    except TimeoutException:
        print("\nDélai dépassé : les résultats Amazon n'ont pas été détectés.")
        print("URL actuelle :", driver.current_url)
        print("Titre de la page :", driver.title)

        if "Sorry! Something went wrong!" in driver.page_source:
            print(
                "Amazon a renvoyé une page d'erreur. "
                "L'accès automatisé est peut-être temporairement limité."
            )
        else:
            print(
                "La page ne contient pas les résultats attendus. "
                "Vérifie la connexion et la structure HTML de la page."
            )

        return []

    except WebDriverException as erreur:
        print("\nUne erreur du navigateur est survenue :", erreur)
        return []

