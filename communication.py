from threading import Timer, Thread, Event, Lock
import consts
import requests
import time


class Communication():
    def __init__(self, port_serie, delai, type_mesure, unite, requete, mutex):
        self.port_serie = port_serie
        self.delai = delai
        self.type = type_mesure
        self.unite = unite
        self.requete = requete
        self.mutex = mutex
        self.thread = Timer(self.delai, self.fonction_depart)

    def recuperer_donnee(self):
        self.mutex.acquire()
        self.port_serie.write(self.requete.encode("utf-8"))
        reponse = self.port_serie.readline().decode("utf-8").splitlines()[0]
        self.mutex.release()
        return reponse

    def envoyer_donnee(self):
        data = {
            "type": self.type,
            "unite": self.unite,
            "donnees": [
                [self.recuperer_donnee(), time.time()]
            ]
        }
        r = requests.post(consts.URL_ENREGISTREMENT, json=data)
        print(data, r.text[:3])

    def fonction_depart(self):
        self.envoyer_donnee()
        self.thread = Timer(self.delai, self.fonction_depart)
        self.thread.start()

    def start(self):
        self.thread.start()

    def cancel(self):
        self.thread.cancel()
