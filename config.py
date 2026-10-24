from pathlib import Path

# Dossier principal du projet
BASE_DIR = Path(__file__).resolve().parent

# Dossiers de stockage
DATA_DIR = BASE_DIR / "data"
EXPORTS_DIR = BASE_DIR / "exports"

# Base de données SQLite
DATABASE_PATH = DATA_DIR / "amazon.db"

# Configuration du scraper
AMAZON_URL = "https://www.amazon.com"
DELAI_ATTENTE = 15
