
from pathlib import Path
from tempfile import NamedTemporaryFile

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from app.scraper.parsing import analyser_produits


html = """
<html>
<body>
    <div data-component-type="s-search-result">
        <h2>
            <a href="https://example.com/clavier">
                <span>Clavier numérique</span>
            </a>
        </h2>
        <span class="a-price">
            <span class="a-offscreen">5 000 FCFA</span>
        </span>
    </div>

    <div data-component-type="s-search-result">
        <h2>
            <a href="https://example.com/souris">
                <span>Souris sans fil</span>
            </a>
        </h2>
        <span class="a-price">
            <span class="a-offscreen">3 000 FCFA</span>
        </span>
    </div>
</body>
</html>
"""

options = Options()
options.add_argument("--headless")

driver = webdriver.Chrome(options=options)

try:
    with NamedTemporaryFile(
        mode="w",
        suffix=".html",
        encoding="utf-8",
        delete=False
    ) as fichier:
        fichier.write(html)
        chemin = Path(fichier.name).as_uri()

    driver.get(chemin)
    produits = analyser_produits(driver)

    print(f"Nombre de produits détectés : {len(produits)}")

    for produit in produits:
        print(produit)
        print("-" * 30)

finally:
    driver.quit()
    if "chemin" in locals():
        Path(fichier.name).unlink(missing_ok=True)
