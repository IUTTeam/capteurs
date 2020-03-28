from threading import Timer, Thread, Event, Lock
import consts
import requests
import time


class CommunicantDistance():
    def __init__(self, port_serie, delai, mutex):
        self.port_serie = port_serie
        self.delai = delai
        self.thread = Timer(self.delai, self.fonction_depart)
        self.mutex = mutex

    def recuperer_distance(self):
        self.mutex.acquire()
        self.port_serie.write(consts.READ_DISTANCE.encode("utf-8"))
        reponse = self.port_serie.readline().decode("utf-8").splitlines()[0]
        self.mutex.release()
        return reponse

    def envoyer_distance(self):
        data = {
            "type": "distance",
            "donnees": [
                [self.recuperer_distance(), time.time()]
            ]
        }
        r = requests.post(consts.URL_ENREGISTREMENT, json=data)
        print(data, r.text)

    def fonction_depart(self):
        self.envoyer_distance()
        self.thread = Timer(self.delai, self.fonction_depart)
        self.thread.start()

    def start(self):
        self.thread.start()

    def cancel(self):
        self.thread.cancel()
