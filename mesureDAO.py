import sqlite3
import consts
import threading


class MesureDAO():
    def __init__(self):
        table_schema = ""
        with open(consts.INITIALISATION_SQL, 'r') as fichier_schema:
            table_schema = fichier_schema.read().replace('\n', '')

        # Connection à la BDD (ou création de celle-ci si elle n'existe pas)
        self.db_connection = sqlite3.connect(consts.NOM_BDD)
        self.db_cursor = self.db_connection.cursor()

        sqlite3.complete_statement(table_schema)
        self.db_cursor.executescript(table_schema)
        self.mutex = threading.Lock()

    def ajouter_mesure(self, type_mesure, unite, mesure, datetime):
        self.mutex.acquire()
        self.db_cursor.execute(
            "INSERT INTO mesures (type_mesure, unite, mesure, insertion_datetime) VALUES (?, ?, ?, ?) ;", (type_mesure, unite, mesure, datetime))
        self.db_connection.commit()
        self.mutex.release()
    
    def get_mesures(self):
        self.mutex.acquire()
        resultat = self.db_cursor.execute("SELECT * FROM mesures ;")
        mesures = [mesure for mesure in resultat]
        self.mutex.release()
        return mesures
    
    def supprimer_mesure(self, datetime):
        self.mutex.acquire()
        self.db_cursor.execute(
            "DELETE FROM mesures WHERE insertion_datetime = ?;", (datetime,))
        self.db_connection.commit()
        self.mutex.release()

