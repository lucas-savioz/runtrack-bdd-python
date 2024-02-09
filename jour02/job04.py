import mysql.connector

# Connexion à la base de données
conn = mysql.connector.connect(
    host="localhost",
    user="votre_utilisateur",
    password="votre_mot_de_passe",
    database="votre_base_de_donnees"
)

# Création d'un curseur pour exécuter des requêtes SQL
cursor = conn.cursor()

# Requête pour récupérer les noms et les capacités de la table "salle"
query = "SELECT nom, capacite FROM salle"

# Exécution de la requête
cursor.execute(query)

# Récupération des résultats
resultats = cursor.fetchall()

# Affichage des résultats en console
for resultat in resultats:
    nom, capacite = resultat
    print(f"Nom de la salle : {nom}, Capacité : {capacite}")

# Fermeture du curseur et de la connexion
cursor.close()
conn.close()