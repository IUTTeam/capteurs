from flask import Flask, render_template, request

import serial
import serial.tools.list_ports
import sys
import time
import datetime
import requests
import consts
import communication
import threading
import mesureDAO
import copy
BAUDRATE = 9600

app = Flask(__name__)

liste_th = []
capteurs_libre = copy.deepcopy(consts.CAPTEURS)
arduino = None
mutex = threading.Lock()


@app.before_first_request
def start():
    global arduino
    liste_port = []
    for port in serial.tools.list_ports.comports():
        liste_port.append(port)

    if len(liste_port) == 0:
        print("Erreur : Pas de port trouvé")
        sys.exit(1)

    arduino = serial.Serial(port=liste_port[0].device, baudrate=BAUDRATE)
    print(arduino.readline().decode("ascii").splitlines()[0])

    dao = mesureDAO.MesureDAO()
    th_temperature = communication.Communication(
        arduino, 5, consts.CAPTEUR_TEMPERATURE, "temperaturetest", mutex)
    th_temperature.start()
    liste_th.append(th_temperature)
    capteurs_libre.remove(consts.CAPTEUR_TEMPERATURE)
    # th_distance = communication.Communication(
    #     arduino, 5, "distancetest", "cm", consts.READ_DISTANCE, mutex)
    # # th_distance.start()
    # th_luminosite = communication.Communication(
    #     arduino, 5, "luminositetest", "pourcent", consts.READ_LUMINOSITE, mutex)
    # th_luminosite.start()

    # liste_th.append(th_distance)
    # liste_th.append(th_luminosite)


@app.route('/')
def index():
    return render_template('index.html', liste=liste_th, capteurs_libre=capteurs_libre)


@app.route('/result', methods=['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      return render_template("result.html", result=result)


@app.route("/modifier/<requete_arduino>")
def modifier(requete_arduino):
    for thread in liste_th:
        if thread.requete == requete_arduino:
            return render_template("modification.html", capteur=thread)
    return "oh nn"


@app.route("/supprimer/<requete_arduino>")
def supprimer(requete_arduino):
    for thread in liste_th:
        if thread.requete == requete_arduino:
            thread.cancel()
            for capteur in consts.CAPTEURS:
                print(capteur)
                if capteur["requete"] == requete_arduino:
                    capteurs_libre.append(capteur)
            liste_th.remove(thread)
            return "OK"
    return "oh nn"


@app.route("/ajout")
def ajout():
    return render_template("ajout.html", capteurs_libre=capteurs_libre)


@app.route("/ajouter", methods=["POST", "GET"])
def ajouter():
    resultat = request.form
    requete = resultat["type"]
    for capteur in capteurs_libre:
        if capteur["requete"] == requete:
            thread = communication.Communication(arduino, int(
                resultat["frequence"]), capteur, resultat["nom"], mutex)
            capteurs_libre.remove(capteur)
            liste_th.append(thread)
            thread.start()
    return "ok"


@app.route("/enregistrer", methods=["POST", "GET"])
def enregistrer():
    resultat = request.form
    print(resultat["requete"])
    for thread in liste_th:
        if thread.requete == resultat["requete"]:
            thread.cancel()
            nouveau_thread = communication.Communication(thread.port_serie, int(
                resultat["frequence"]), thread.type, thread.unite, thread.requete, thread.mutex)
            liste_th.remove(thread)
            liste_th.append(nouveau_thread)
            nouveau_thread.start()
            print(liste_th)
    return "OK"


def start_runner():
    def start_loop():
        demarre = False
        while not demarre:
            print("Status : Démarrage")
            try:
                r = requests.get('http://127.0.0.1:5000/')
                if r.status_code == 200:
                    print("Status : OK Serveur démarré")
                    demarre = True
            except:
                print("Status : Redémarrage")
            time.sleep(2)
    thread = threading.Thread(target=start_loop)
    thread.start()


if __name__ == '__main__':
    start_runner()
    app.run(debug=True)
