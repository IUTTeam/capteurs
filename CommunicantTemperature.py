from threading import Timer, Thread, Event
import consts
import requests
import time


class CommunicantTemperature():
    def __init__(self, port_serie, delai):
        self.port_serie = port_serie
        self.delai = delai
        self.thread = Timer(self.delai, self.fonction_depart)

    def recuperer_temperature(self):
        self.port_serie.write(consts.READ_ANALOG_TEMP.encode("utf-8"))
        reponse = self.port_serie.readline().decode("utf-8").splitlines()[0]
        return reponse

    def envoyer_temperature(self):
        data = {
            "type": "temperature",
            "donnees": [
                [self.recuperer_temperature(), time.time()]
            ]
        }
        r = requests.post(consts.URL_ENREGISTREMENT, json=data)
        print(data, r.text)
    
    def fonction_depart(self):
        self.envoyer_temperature()
        self.thread = Timer(self.delai, self.fonction_depart)
        self.thread.start()

    def start(self):
        self.thread.start()
    
    def cancel(self):
        self.thread.cancel()