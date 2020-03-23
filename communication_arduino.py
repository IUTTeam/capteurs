import serial
import serial.tools.list_ports
import sys
import time
import datetime
import requests
import consts

BAUDRATE = 9600

# Programme de communication python arduino : ArduinoModule doit être dans l'arduino

liste_port = []
for port in serial.tools.list_ports.comports():
    liste_port.append(port)

if len(liste_port) == 0:
    print("Erreur : Pas de port trouvé")
    sys.exit(1)

with serial.Serial(port=liste_port[0].device, baudrate=BAUDRATE) as arduino:
    print(arduino.readline().decode("ascii").splitlines()[0])
    while True:
        message = consts.READ_ANALOG_TEMP
        arduino.write(message.encode("utf-8"))
        reponse = arduino.readline().decode("utf-8").splitlines()[0]
        data = {
            "type": "temperature",
            "donnees": [
                [reponse, time.time()]
            ]
        }
        r = requests.post(consts.URL_ENREGISTREMENT, json=data)
        print(data, r.text)
        time.sleep(2)
