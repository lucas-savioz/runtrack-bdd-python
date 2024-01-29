CREATE TABLE etudiant (id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY, nom VARCHAR(100), prenom VARCHAR(100), email VARCHAR(255) NOT NULL UNIQUE);


mysql> SHOW tables;
+------------------------+
| Tables_in_laplateforme |
+------------------------+
| etudiant               |
+------------------------+
1 row in set (0.01 sec)

mysql>