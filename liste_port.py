import serial
import serial.tools.list_ports
import sys

BAUDRATE = 9600

liste_port = []
for port in serial.tools.list_ports.comports():
    liste_port.append(port)

if len(liste_port) == 0:
    print("Erreur : Pas de port trouvé")
    sys.exit(1)

with serial.Serial(port=liste_port[0].device, baudrate=BAUDRATE) as arduino:
    print(arduino.readline().decode("ascii").splitlines()[0])
    while True:
        print(arduino.readline().decode("ascii").splitlines()[0])

