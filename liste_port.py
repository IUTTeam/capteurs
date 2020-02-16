import serial
import serial.tools.list_ports

# Liste le port sur lesquel l'arduino est branché
for port in serial.tools.list_ports.comports():
    print(port.device)
