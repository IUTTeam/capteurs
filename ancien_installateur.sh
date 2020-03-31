#!/bin/bash

errorFlag=false
# détection des erreurs

echo "  +---------------------------------------------------------------------------+"
echo -e "\e[90m#\e[0m !         Programme d'installation des prérequis pour le déploiement        !"
echo -e "\e[90m#\e[0m !          du programme de lecture des capteurs sur le Raspberry Pi         !"
echo -e "\e[90m#\e[0m +---------------------------------------------------------------------------+"
echo -e "\e[90m##############################################################################\e[0m"

echo -e "\e[1mTous les fichiers requis à l'installation doivent se trouver dans \e[1;32m/projetTut/\e[0m\e[1m.\e[0m"

if [ "$EUID" -ne 0 ] ; then
	echo -e "\e[1;31mCe programme doit être lancé par le root. Fin du programme.\e[0m"
	echo -e "\e[32mUsage :\e[0m sudo ${0}"
	exit 1
fi

echo "Configuration du Wi-Fi :"
options=("usage privé" "usage à l'IUT" "ne pas configurer le Wi-Fi")
select choix in "${options[@]}"
do
    case $choix in
        "usage privé")
			echo "Veuillez saisir les informations de connexion au WiFi :"
			read -p "SSID du point d'accès Wi-Fi : " ssid
			read -sp "mot de passe ...............: " motdepasse
			echo # On passe à la ligne.

			echo "Configuration Wi-Fi, changement du fichier wpa-supplicant…"

			echo "network={
			    ssid="$ssid"
			    psk="$motdepasse"
			}" >> /etc/wpa_supplicant/wpa_supplicant.conf && echo -e "\e[32m→ fait !\e[0m" || { echo -e "\e[1;31m→ ÉCHEC.\e[0m"; errorFlag=true; };
			# > pour remplacer le contenu d'un fichier, >> pour ajouter au contenu existant.

            break
            ;;
        "usage à l'IUT")
			echo -e "\e[1;31mPrenez note que la connexion à l'IUT n'a pas été testée.\e[0m"
            echo "Configuration du WiFi pour l'IUT. Veuillez saisir les informations de connexion au WiFi (WiFi de l'IUT, WPA-EAP) :"
			read -p 'identifiant .: ' identifiant
			read -sp 'mot de passe : ' motdepasse
			echo # On passe à la ligne.

			echo "Configuration WiFi, changement du fichier wpa-supplicant…"

			echo "network={
			  ssid="eduroam"
			  scan_ssid=1
			  key_mgmt=WPA-EAP
			  ca_cert=
			  identity="$identifiant"
			  password="$motdepasse"
			  eap=PEAP
			  phase1="peaplabel=auto peapver=0"
			  phase2="auth=MSCHAPV2"
			  priority=1
			}" >> /etc/wpa_supplicant/wpa_supplicant.conf && echo -e "\e[32m→ fait !\e[0m" || { echo -e "\e[1;31m→ ÉCHEC.\e[0m"; errorFlag=true; };

            break
            ;;
        "ne pas configurer le Wi-Fi")
			echo "Pas de configuration du Wi-Fi."
			echo -e "\e[32m→ fait !\e[0m"
            break
            ;;
        *) echo "Le choix $REPLY n'existe pas. Sélectionnez un chiffre entre 1 et 3.";;
    esac
done

echo "Installation du fichier de lancement automatique de l'application dans init.d…"
# on ajoute notre fichier startup dans le répertoire des scripts à lancer au démarrage.
# et on rend notre fichier startup executable
cp /projetTut/startup /etc/init.d/startup && chmod 555 /etc/init.d/startup && echo -e "\e[32m→ fait !\e[0m" || { echo -e "\e[1;31m→ ÉCHEC.\e[0m"; errorFlag=true; };
# On n'ajoute notre fichier startup dans la liste des scripts à lancer au démarrage QUE si tout le reste de l'installation réussit.

echo "Configuration des fichiers locaux de /projetTut…"
chmod 555 /projetTut/lanceurLectureCapteurs.sh && echo -e "\e[32m→ fait !\e[0m" || { echo -e "\e[1;31m→ ÉCHEC.\e[0m"; errorFlag=true; };

# echo "Installation de Python…"
# apt install python python3 python-dev build-essential && echo -e "\e[32m→ fait !\e[0m" || { echo -e "\e[1;31m→ ÉCHEC.\e[0m"; errorFlag=true; };

# echo "Installation du gestionnaire de bibliothèques Python “PIP”…"
# apt install python-pip && echo -e "\e[32m→ fait !\e[0m" || { echo -e "\e[1;31m→ ÉCHEC.\e[0m"; errorFlag=true; };

# QUICK-FIX PYTHON 3

echo "Installation de Python 3…"
apt install python3 python3-dev && echo -e "\e[32m→ fait !\e[0m" || { echo -e "\e[1;31m→ ÉCHEC.\e[0m"; errorFlag=true; };

echo "Installation du gestionnaire de bibliothèques Python 3 “PIP3”…"
apt install python3-pip && echo -e "\e[32m→ fait !\e[0m" || { echo -e "\e[1;31m→ ÉCHEC.\e[0m"; errorFlag=true; };

echo "Installation des bibliothèques Python 3 requises à la communication avec l'Arduino…"
pip3 install pyserial && echo -e "\e[32m→ fait !\e[0m" || { echo -e "\e[1;31m→ ÉCHEC.\e[0m"; errorFlag=true; };

echo "Installation des bibliothèques Python 3 requises à l'envoi de requêtes HTML…"
pip3 install requests && echo -e "\e[32m→ fait !\e[0m" || { echo -e "\e[1;31m→ ÉCHEC.\e[0m"; errorFlag=true; };

echo "Installation des bibliothèques Python requises à la mise en place d'une page Web de configuration…"
pip3 install flask && echo -e "\e[32m→ fait !\e[0m" || { echo -e "\e[1;31m→ ÉCHEC.\e[0m"; errorFlag=true; };

echo "Instalation des utilitaires de compilation requis à l'instalation des bibliothèques Python 3 SQLite…"
apt install build-essential python-dev git scons swig && echo -e "\e[32m→ fait !\e[0m" || { echo -e "\e[1;31m→ ÉCHEC.\e[0m"; errorFlag=true; };

echo "Installation de SQLite…"
apt install sqlite3 libsqlite3-dev && echo -e "\e[32m→ fait !\e[0m" || { echo -e "\e[1;31m→ ÉCHEC.\e[0m"; errorFlag=true; };

echo "Installation des librairies Python 3 SQLite…"
pip install pysqlite && echo -e "\e[32m→ fait !\e[0m" || { echo -e "\e[1;31m→ ÉCHEC.\e[0m"; errorFlag=true; };

echo "Création de la base de données SQLite…"
python /projetTut/database-initialisation.py && chmod 666 /projetTut/BDD_PROJET_TUT_PI && echo -e "\e[32m→ fait !\e[0m" || { echo -e "\e[1;31m→ ÉCHEC.\e[0m"; errorFlag=true; };

echo -e "\e[1;32mInstallation terminée.\e[0m"

if [ "$errorFlag" = true ] ; then
    echo -e "\e[1;31mLe programme d'installation s'est terminé en rencontrant des erreurs.\e[0m"

    echo "Pour éviter tout risque, le programme de lecture des capteurs n'a pas été ajouté à la liste des programmes à charger au démarrage."
else
	echo -e "\e[1;32mLe programme d'installation s'est terminé sans rencontrer d'erreur.\e[0m"

	# ajout de notre fichier startup dans la liste des scripts à lancer au démarrage.
	#######################################################################################################################
	# POUR QU'UN PROBLÈME D'INSTALLATION NE SOIT PAS HANDICAPANT, IL FAUDRAIT PLACER CETTE LIGNE EN TOUTE FIN DE FICHIER. #
	# DE CETTE FAÇON, SI UNE ÉTAPE DE L'INSTALLATION ÉCHOUE, LE PROGRAMME N'EST PAS LANCÉ AU DÉMARRAGE.                   #
	#######################################################################################################################
	echo "Ajout du fichier de lancement automatique dans la liste des programmes à lancer automatiquement…"
	update-rc.d startup defaults && echo -e "\e[32m→ fait !\e[0m" || { echo -e "\e[1;31m→ ÉCHEC.\e[0m"; errorFlag=true; };

	echo "Un redémarrage est nécessaire pour compléter l'installation."
	echo "Redémarrage…"

	reboot
fi
