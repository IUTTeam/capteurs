import serial
import serial.tools.list_ports
import sys
import time
import datetime
import requests
import consts
import CommunicantTemperature
import CommunicantDistance
import threading
BAUDRATE = 9600

# Programme de communication python arduino : ArduinoModule doit être dans l'arduino

liste_port = []
for port in serial.tools.list_ports.comports():
    liste_port.append(port)

if len(liste_port) == 0:
    print("Erreur : Pas de port trouvé")
    sys.exit(1)

arduino = serial.Serial(port=liste_port[0].device, baudrate=BAUDRATE)
print(arduino.readline().decode("ascii").splitlines()[0])
mutex = threading.Lock()
comm = CommunicantTemperature.CommunicantTemperature(arduino, 2, mutex)
comm.start()
comm2 = CommunicantDistance.CommunicantDistance(arduino, 1, mutex)
comm2.start()
