#-*-coding:utf8-*-

import sqlite3

# Paramètres de la base de données (attention, ce nom apparait dans le programme d'installation).
NOM_BDD = "BDD_PROJET_TUT_PI"

# Initialistaion de la base de données
INITIALISATION_SQL = "creation-table.sql"

# Lecture du schema de la base de données (copie dans une variable et remplacement des "\n" par des " ").
TableSchema = ""
with open(INITIALISATION_SQL, 'r') as SchemaFile :
	TableSchema = SchemaFile.read().replace('\n', '')

# Connection à la BDD (ou création de celle-ci si elle n'existe pas)
db_connection = sqlite3.connect(NOM_BDD)
db_cursor = db_connection.cursor()

# Création des tables
sqlite3.complete_statement(TableSchema)
db_cursor.executescript(TableSchema)

test = db_cursor.execute("SELECT name FROM sqlite_master WHERE type = \"table\"")
for i in test:
	print(i)

db_cursor.execute("INSERT INTO mesures (type_mesure, unite, mesure, insertion_datetime) VALUES ('test', 'cm', 33.2, 1568865886);")
db_connection.commit()

test = db_cursor.execute("SELECT * FROM mesures")
for i in test:
	print(i)

# Fermeture de la Base de données
db_cursor.close()
db_connection.close()
