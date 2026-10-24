import sqlite3
from config import DATABASE_PATH

connexion = sqlite3.connect(DATABASE_PATH)

resultat = connexion.execute(
"SELECT name FROM sqlite_master WHERE type='table'"
).fetchall()

print("Tables présentes dans la base :", resultat)

connexion.close()
