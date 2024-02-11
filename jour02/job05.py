import mysql.connector

# Connexion à la base de données
database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="LaPlateforme"
)

# Création d'un curseur pour exécuter des requêtes SQL
cursor = database.cursor()

# Requête pour récupérer les superficies des différents étages
query = "SELECT SUM(superficie) FROM etage"

# Exécute la requête
cursor.execute(query)

# Variable x qui récupére le résultat
x = cursor.fetchone()[0]

# Fermeture du curseur et de la connexion à la base de données
cursor.close()
database.close()

# Affichage du résultat
print(f"La superficie de La Plateforme est de {x} m2.")
