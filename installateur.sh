#!/bin/bash

errorFlag=false
# détection des erreurs

titre="Installation programme projet tutoré"
# titre de l'écran de fond.
# finalement j'utilise whiptail plutôt que dialog.
# je connaissais pas mais c'est plus simple à utiliser.

function echec ()
{
	whiptail --title "Erreur" --backtitle "$titre" --ok-button "poursuivre" --msgbox "L'opération \"$1\" à échoué !" 8 78
	errorFlag=true
}

function reussite ()
{
	whiptail --title "Réussite" --backtitle "$titre" --ok-button "poursuivre" --msgbox "L'opération \"$1\" a été accomplie avec succès !" 8 78
}

function majprogress ()
{
	echo $2 | whiptail --title "Installation" --backtitle "$titre" --gauge "$1" 6 78 0
	# la barre de progression va prendre la valeur d'avancement contenue dans $2.
}

echo "  +---------------------------------------------------------------------------+"
echo -e "\e[90m#\e[0m !         Programme d'installation des prérequis pour le déploiement        !"
echo -e "\e[90m#\e[0m !          du programme de lecture des capteurs sur le Raspberry Pi         !"
echo -e "\e[90m#\e[0m +---------------------------------------------------------------------------+"
echo -e "\e[90m##############################################################################\e[0m"

echo -e "\e[1;31mSi ces lignes sont lisibles et que l'interface de l'installateur ne se lance pas, une erreur est survenue.\e[0m"

TERM=ansi # pour éviter les erreurs d'affichage dans le terminal avec whiptail.

if [ "$EUID" -ne 0 ] ; then

	whiptail --title "Erreur" --backtitle "$titre" --ok-button "quitter" --msgbox "Ce programme doit être lancé par le root.\nFin du programme.\nUsage : sudo ${0}" 11 78

	clear
	exit 1
fi

operation="Configuration du Wi-Fi"
	
OPTION=$(whiptail --title "$operation" --backtitle "$titre" --menu "Parametres de configuration du Wi-Fi" 15 78 4 \
"1" "usage privé" \
"2" "usage à l'IUT" \
"3" "ne pas configurer le Wi-Fi" 3>&1 1>&2 2>&3) # ATTENTION !! Les redirections sont parsées DE DROITE À GAUCHE… (ici on fusionne, donc ça va.)
 
exitstatus=$?
if [ $exitstatus = 0 ]; then
	case $OPTION in
		1)
			ssid=$(whiptail --title "$operation" --backtitle "$titre" --inputbox "Veuillez saisir les informations de connexion au WiFi\nSSID du point d'accès Wi-Fi :" 10 78 3>&1 1>&2 2>&3)
			 
			exitstatus=$?
			if [ $exitstatus = 0 ]; then

				motdepasse=$(whiptail --title "$operation" --backtitle "$titre" --passwordbox "Veuillez saisir les informations de connexion au WiFi\nmot de passe :" 10 78 3>&1 1>&2 2>&3)

				exitstatus=$?
				if [ $exitstatus = 0 ]; then

					echo "network={
					  ssid="$ssid"
					  psk="$motdepasse"
					}" >> /etc/wpa_supplicant/wpa_supplicant.conf && reussite "$operation" || echec "$operation privé écriture WPA supplicant"
					# > pour remplacer le contenu d'un fichier, >> pour ajouter au contenu existant.

				else
					echec "$operation privé annulée au mot de passe"
				fi

			else
				echec "$operation annulée au SSID"
			fi
			
			;;
		2)
			whiptail --title "Avertissement" --backtitle "$titre" --msgbox "Prenez note que la connexion à l'IUT n'a pas été testée." 8 78

			identifiant=$(whiptail --title "$operation" --backtitle "$titre" --inputbox "Veuillez saisir les informations de connexion au WiFi eduroam\nidentifiant de connexion :" 10 78 3>&1 1>&2 2>&3)

			exitstatus=$?
			if [ $exitstatus = 0 ]; then

				motdepasse=$(whiptail --title "$operation" --backtitle "$titre" --passwordbox "Veuillez saisir les informations de connexion au WiFi\nmot de passe :" 10 78 3>&1 1>&2 2>&3)

				exitstatus=$?
				if [ $exitstatus = 0 ]; then

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
					}" >> /etc/wpa_supplicant/wpa_supplicant.conf && reussite "$operation" || echec "$operation IUT écriture WPA supplicant"

				else
					echec "$operation IUT annulée au mot de passe"
				fi

			else
				echec "$operation IUT annulée à l'identifiant"
			fi			

			;;
        *)
			whiptail --title "Avertissement" --backtitle "$titre" --msgbox "Aucun réseau Wi-Fi ne sera configuré." 8 78
			;;
    esac
else
    whiptail --title "Avertissement" --backtitle "$titre" --msgbox "Aucun réseau Wi-Fi ne sera configuré." 8 78
fi

operation="Installation du fichier de lancement automatique de l'application dans init.d"
# on ajoute notre fichier startup dans le répertoire des scripts à lancer au démarrage.
# et on rend notre fichier startup executable
cp /projetTut/startup /etc/init.d/startup && chmod 555 /etc/init.d/startup || echec "$operation"
# On n'ajoute notre fichier startup dans la liste des scripts à lancer au démarrage QUE si tout le reste de l'installation réussit.

operation="Configuration des fichiers locaux de /projetTut"
majprogress "$operation" 15 && chmod 555 /projetTut/lanceurLectureCapteurs.sh || echec "$operation"

operation="Installation de Python"
majprogress "$operation" 25 && apt install python python3 python-dev build-essential || echec "$operation"

operation="Installation du gestionnaire de bibliothèques Python “PIP”"
majprogress "$operation" 35 && apt install python-pip || echec "$operation"

operation="Installation des bibliothèques Python requises à la communication avec l'Arduino"
majprogress "$operation" 45 && pip install pyserial || echec "$operation"

operation="Installation des bibliothèques Python requises à l'envoi de requêtes HTML"
majprogress "$operation" 55 && pip install requests || echec "$operation"

operation="Instalation des utilitaires de compilation requis à l'instalation des bibliothèques Python SQLite…"
majprogress "$operation" 65 && apt install build-essential python-dev git scons swig || echec "$operation"

operation="Installation de SQLite"
majprogress "$operation" 75 && apt install sqlite3 libsqlite3-dev || echec "$operation"

operation="Installation des librairies Python SQLite"
majprogress "$operation" 85 && pip install pysqlite || echec "$operation"

operation="Création de la base de données SQLite"
majprogress "$operation" 95 && python /projetTut/database-initialisation.py && chmod 666 /projetTut/BDD_PROJET_TUT_PI || echec "$operation"

reussite "installation"

clear

if [ "$errorFlag" = true ] ; then

	whiptail --title "Erreur" --backtitle "$titre" --ok-button "quitter" --msgbox "Le programme d'installation s'est terminé en rencontrant des erreurs.\nPour éviter tout risque, le programme de lecture des capteurs n'a pas été ajouté à la liste des programmes à charger au démarrage." 12 78

    echo -e "\e[1;31mLe programme d'installation s'est terminé en rencontrant des erreurs.\e[0m"
    echo "Pour éviter tout risque, le programme de lecture des capteurs n'a pas été ajouté à la liste des programmes à charger au démarrage."

    exit 1

else

	whiptail --title "Réussite" --backtitle "$titre" --ok-button "terminer" --msgbox "Le programme d'installation s'est terminé sans rencontrer d'erreur.\nAjout du fichier de lancement automatique dans la liste des programmes à lancer automatiquement…" 12 78

	# ajout de notre fichier startup dans la liste des scripts à lancer au démarrage.
	#######################################################################################################################
	# POUR QU'UN PROBLÈME D'INSTALLATION NE SOIT PAS HANDICAPANT, IL FAUDRAIT PLACER CETTE LIGNE EN TOUTE FIN DE FICHIER. #
	# DE CETTE FAÇON, SI UNE ÉTAPE DE L'INSTALLATION ÉCHOUE, LE PROGRAMME N'EST PAS LANCÉ AU DÉMARRAGE.                   #
	#######################################################################################################################
	update-rc.d startup defaults || echec "Ajout du fichier de lancement automatique dans la liste des programmes à lancer automatiquement"

	whiptail --title "Redémarrage…" --backtitle "$titre" --infobox "Un redémarrage est nécessaire pour compléter l'installation.\n\nRedémarrage en cours…" 10 78

	reboot
fi
