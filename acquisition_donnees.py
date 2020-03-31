from flask import Flask, render_template, request, redirect, url_for

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

threads_en_cours = []
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
    # connection à l'arduino par le port série
    arduino = serial.Serial(port=liste_port[0].device, baudrate=BAUDRATE)
    print(arduino.readline().decode("ascii").splitlines()[0])

    dao = mesureDAO.MesureDAO()

    # création d'une première récolte de température
    th_temperature = communication.Communication(
        arduino, 5, consts.CAPTEUR_TEMPERATURE, "temperature", mutex)
    th_temperature.start()
    # ajout à la liste des acquisitions en cours
    threads_en_cours.append(th_temperature)
    capteurs_libre.remove(consts.CAPTEUR_TEMPERATURE)

# page d'accueil : avec la liste des données mesurées
@app.route('/')
def index():
    return render_template('index.html', liste=threads_en_cours, capteurs_libre=capteurs_libre)

# page pour modifier les paramètres d'un capteur
@app.route("/modifier/<requete_arduino>")
def modifier(requete_arduino):
    for thread in threads_en_cours:
        if thread.requete == requete_arduino:
            return render_template("modification.html", capteur=thread)
    return "oh nn"

# page appelée pour supprimer une acquisition de données
@app.route("/supprimer/<requete_arduino>")
def supprimer(requete_arduino):
    for thread in threads_en_cours:
        if thread.requete == requete_arduino:
            for capteur in consts.CAPTEURS:
                if capteur["requete"] == requete_arduino:
                    print(capteur)
                    capteurs_libre.append(capteur)
            threads_en_cours.remove(thread)
            print(threads_en_cours)
            thread.cancel()
            return render_template("ok.html")
    return "oh nn"

# page pour ajouter une acquisition de données
@app.route("/ajout")
def ajout():
    return render_template("ajout.html", capteurs_libre=capteurs_libre)

#page appelée qui ajoute l'acquisition de données
@app.route("/ajouter", methods=["POST", "GET"])
def ajouter():
    resultat = request.form
    requete = resultat["type"]
    for capteur in capteurs_libre:
        if capteur["requete"] == requete:
            thread = communication.Communication(arduino, float(
                resultat["frequence"]), capteur, resultat["nom"], mutex)
            capteurs_libre.remove(capteur)
            thread.start()
            threads_en_cours.append(thread)
    return render_template("ok.html")

# page appelée qui enregistre les modifications
@app.route("/enregistrer", methods=["POST", "GET"])
def enregistrer():
    resultat = request.form
    for thread in threads_en_cours:
        if thread.requete == resultat["requete"]:
            thread.cancel()
            requete = resultat["requete"]
            for capteur in consts.CAPTEURS:
                if capteur["requete"] == requete:
                    nouveau_thread = communication.Communication(thread.port_serie, float(
                        resultat["frequence"]), capteur, resultat["nom-donnee"], thread.mutex)
            threads_en_cours.remove(thread)
            threads_en_cours.append(nouveau_thread)
            nouveau_thread.start()
            print(threads_en_cours)
    return render_template("ok.html")


# fonction pour démarrer l'acquisition des données avec l'arduino
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
    app.run(host="0.0.0.0")
