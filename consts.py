READ_ANALOG_TEMP = "1"
READ_DISTANCE = "2"
READ_LUMINOSITE = "3"

CAPTEUR_TEMPERATURE = {"type": "temperaturetest", "unite": "C", "requete": READ_ANALOG_TEMP}
CAPTEUR_DISTANCE    = {"type": "distancetest", "unite": "cm", "requete": READ_DISTANCE}
CAPTEUR_LUMINOSITE  = {"type": "luminositetest", "unite": "pourcent", "requete": READ_LUMINOSITE}

CAPTEURS = [CAPTEUR_TEMPERATURE, CAPTEUR_DISTANCE, CAPTEUR_LUMINOSITE]

URL_ENREGISTREMENT = "https://service.frfr.duckdns.org/send_data"

NOM_BDD = "BDD_PROJET_TUT_PI"
INITIALISATION_SQL = "creation-table.sql"
