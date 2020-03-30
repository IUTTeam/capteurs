from threading import Timer, Thread, Event, Lock
import consts
import requests
import time
import mesureDAO


class Communication():
    def __init__(self, port_serie, delai, capteur, nom_mesure, mutex):
        self.port_serie = port_serie
        self.delai = delai
        self.type = capteur["type"]
        self.unite = capteur["unite"]
        self.requete = capteur["requete"]
        self.nom_mesure = nom_mesure
        self.mutex = mutex
        self.thread = Timer(self.delai, self.fonction_depart)

    def recuperer_donnee(self):
        self.mutex.acquire()
        self.port_serie.write(self.requete.encode("utf-8"))
        reponse = self.port_serie.readline().decode("utf-8").splitlines()[0]
        self.mutex.release()
        return reponse

    def envoyer_donnee(self):
        mesure = self.recuperer_donnee()
        time_mesure = time.time()
        data = {
            "type": self.nom_mesure,
            "unite": self.unite,
            "donnees": [
                [mesure, time_mesure]
            ]
        }
        mesure_envoyee = False
        try:
            reponse = requests.post(consts.URL_ENREGISTREMENT, json=data)
            mesure_envoyee = reponse.text[:3] == "Don"
        except requests.ConnectionError as connection_error:
            print("Erreur de connection")
            mesure_envoyee = False
        if (mesure_envoyee):
            print(time.asctime(time.gmtime(time_mesure)), self.nom_mesure, "OK")
            dao = mesureDAO.MesureDAO()
            liste_mesures = dao.get_mesures()
            for mesure in liste_mesures:
                data = {
                    "type": mesure[0],
                    "unite": mesure[1],
                    "donnees": [
                        [mesure[2], mesure[3]]
                    ]
                }
                envoi = False
                try:
                    reponse = requests.post(
                        consts.URL_ENREGISTREMENT, json=data)
                    envoi = reponse.text[:3] == "Don"
                except requests.ConnectionError as connection_error:
                    envoi = False
                if envoi:
                    dao.supprimer_mesure(mesure[3])

        else:
            print(time.asctime(time.gmtime(time_mesure)), self.nom_mesure, "KO")
            dao = mesureDAO.MesureDAO()
            dao.ajouter_mesure(self.nom_mesure, self.unite, mesure, time_mesure)

    def fonction_depart(self):
        self.envoyer_donnee()
        self.thread = Timer(self.delai, self.fonction_depart)
        self.thread.start()

    def start(self):
        self.thread.start()

    def cancel(self):
        self.thread.cancel()
