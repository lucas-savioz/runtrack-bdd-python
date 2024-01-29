mysql> SHOW COLUMNS FROM etudiant;
+--------+--------------+------+-----+---------+----------------+
| Field  | Type         | Null | Key | Default | Extra          |
+--------+--------------+------+-----+---------+----------------+
| id     | int          | NO   | PRI | NULL    | auto_increment |
| nom    | varchar(100) | YES  |     | NULL    |                |
| prenom | varchar(100) | YES  |     | NULL    |                |
| email  | varchar(255) | NO   | UNI | NULL    |                |
+--------+--------------+------+-----+---------+----------------+
4 rows in set (0.00 sec)

mysql>