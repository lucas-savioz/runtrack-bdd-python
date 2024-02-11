import mysql.connector

# Connection à la base de données
database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="LaPlateforme"
)

# Création d'un curseur pour exécuter la requête SQL
cursor = database.cursor()

# Requête pour récupérer les noms et les capacités de la table "salle"
query = "SELECT nom, capacite FROM salle"

# Exécution de la requête
cursor.execute(query)

# Récupération des résultats
results = cursor.fetchall()

# Affichage des résultats en console
for result in results:
    name, capacity = result
    print(f"Nom de la salle : {name}, Capacité : {capacity}")

# Fermeture du curseur et de la base de donnée
cursor.close()
database.close()