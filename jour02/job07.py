import mysql.connector

class Employe:
    def __init__(self, host, user, password, database):
        self.mydb = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.mydb.cursor()

    def get_employees_services(self):
        query = """
            SELECT e.*, s.nom AS service_nom
            FROM employe e
            INNER JOIN service s ON e.id_service = s.id
        """
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def close_database(self):
        self.cursor.close()
        self.mydb.close()

# Utilisation de la classe Employe
employe_manager = Employe(host="localhost", user="root", password="root", database="job07")
employees_with_service = employe_manager.get_employees_services()
for employee in employees_with_service:
    print("Nom:", employee[1])
    print("Prénom:", employee[2])
    print("Salaire:", employee[3])
    print("Service:", employee[5])
    print("-" * 20)

# Ferme la connexion une fois fini
employe_manager.close_database()
