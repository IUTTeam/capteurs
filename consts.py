READ_ANALOG_TEMP = "1"
READ_DISTANCE = "2"
READ_LUMINOSITE = "3"
READ_ANALOG_TEMP_EXT = "4"

CAPTEUR_TEMPERATURE = {"type": "temperature", "unite": "C", "requete": READ_ANALOG_TEMP}
CAPTEUR_DISTANCE    = {"type": "distance", "unite": "cm", "requete": READ_DISTANCE}
CAPTEUR_LUMINOSITE  = {"type": "luminosite", "unite": "pourcent", "requete": READ_LUMINOSITE}
CAPTEUR_TEMPERATURE_EXT  = {"type": "temperature-exterieur", "unite": "C", "requete": READ_ANALOG_TEMP_EXT}

CAPTEURS = [CAPTEUR_TEMPERATURE, CAPTEUR_DISTANCE, CAPTEUR_LUMINOSITE, CAPTEUR_TEMPERATURE_EXT]

URL_ENREGISTREMENT = "https://service.frfr.duckdns.org/send_data"

NOM_BDD = "BDD_PROJET_TUT_PI"
INITIALISATION_SQL = "/projetTut/creation-table.sql"
