from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def creer_driver():
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--lang=fr-FR")

    driver = webdriver.Chrome(options=options)
    return driver