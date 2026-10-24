from selenium import webdriver
from selenium.webdriver.chrome.options import Options
 
def creer_driver():
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--lang=fr-FR")
 
    # Réduire les signes d'automatisation
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
 
    # User-agent d'un Chrome normal (adapte la version à la tienne)
    options.add_argument(
        "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/130.0.0.0 Safari/537.36"
    )
 
    driver = webdriver.Chrome(options=options)
    return driver
 