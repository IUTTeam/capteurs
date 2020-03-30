# capteurs

> Pensez à lire la documentation en entier, ça peut toujours servir (RTFM).

## Script d'acquisition des données

Acquisition des données via un Arduino et un Raspberry Pi

Il faut installer `pyserial` pour communiquer avec l'Arduino :
```BASH
pip3 install pyserial
```

> La carte arduino doit contenir le programme `ArduinoModule` pour fonctionner avec le Raspberry

## Interface d'administration

Il faut `flask` pour gérer les capteurs :
```BASH
pip3 install flask
```
La gestion des capteurs se fait via un navigateur grâce à un mini serveur web sur le Raspberry.

### Fonctionnement de flask
- les données statiques (css) se trouvent dans le dossier `static`
- les templates se trouvent dans le dossier `templates`

## Programme d'installation

### Copie des fichiers sur le Raspberry-Pi

Tous les fichiers contenu dans ce répertoire sont à copier sur le Rapsberry-Pi dans `/ProjetTut`.

Il est nécessaire de ne pas changer les noms des fichiers de ce répertoire, ou, le cas échéant, d'ouvrir tous les fichiers afin de s'assurer que toutes les occurrences du nom de fichier modifié ont elles-aussi été modifiées (les occurrences sont indiquées dans des commentaires dans les fichiers où elles se trouvent).

Le fichier du programme d'installation doit être exécutable (pas besoin de s'occuper des autres fichiers, l'installateur s'en charge tout seul).

### Installation et configuration

Une fois la copie terminée, il est possible d'installer tous les prérequis via la commande :

Pour avoir l'installateur doté d'une interface affichable en console :

```BASH
sudo ./installateur.sh
```

Pour avoir l'ancien installateur en texte :

```BASH
sudo ./ancien_installateur.sh # n'exécutez pas cette commande si la première à fonctionné.
```

Ce programme se chargera automatiquement de :

* configurer le Wi-Fi (l'utilisateur peut choisir de configurer un Wi-Fi privé, *eduroam* ou de ne pas le configurer) ;
* installer toutes les bibliothèques Python requises pour le fonctionnement des scripts (dont `pyserial`, `requests`, `sqlite3`, etc.) ;
* installer SQLite pour la gestion interne d'une mini base de données ;
* créer et configurer la mini base de donnée ;
* et si tout s'est bien passé, configurer l'exécution automatique au démarrage du programme de relevé de mesures.

Le programme d'installation détecte automatiquement toute erreur lors de l'installation et annule la configuration automatique des scripts au démarrage en cas de problème.

Deux versions du programme installateur sont employables : l'une d'entre elle en mode texte pour pouvoir installer le programme dans l'hypothèse où l'autre installateur ne fonctionnerait pas, l'autre est un installateur doté d'une interface plus conviviale. Je pensais employer `dialog`, mais j'ai finalement utilisé `whiptail`. Il est plus léger et offre moins de possibilités, mais il sera parfait pour une utilisation sur Raspberry-Pi et ne requiert (normalement) pas d'installation de paquets supplémentaires.

