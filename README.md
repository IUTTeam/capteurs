# capteurs

> Pensez à lire la documentation *en entier* avant d'entreprendre quoi que ce soit, ça peut toujours servir (RTFM).

## Installation manuelle des modules complémentaires

> **NOTA BENE** : Cette procédure n'est à suivre que pour des installations qui ont déjà été faites avec une version ancienne de l'installateur voire directement à la main.

### Script d'acquisition des données

Acquisition des données via un Arduino et un Raspberry Pi

Il faut installer `pyserial` pour communiquer avec l'Arduino :
```BASH
pip3 install pyserial
```

> La carte arduino doit contenir le programme `ArduinoModule` pour fonctionner avec le Raspberry

### Interface d'administration

Il faut `flask` pour gérer les capteurs :
```BASH
pip3 install flask
```
La gestion des capteurs se fait via un navigateur grâce à un mini serveur web sur le Raspberry.

#### Fonctionnement de flask
- les données statiques (css) se trouvent dans le dossier `static`
- les templates se trouvent dans le dossier `templates`

## Programme d'installation automatique, dont les modules complémentaires

> **NOTA BENE** : Cette procédure est *la seule à suivre* pour toute nouvelle installation du projet.

### Copie des fichiers sur le Raspberry-Pi

Tous les fichiers contenu dans ce répertoire sont à copier sur le Rapsberry-Pi dans `/ProjetTut`.

Il est nécessaire de ne pas changer les noms des fichiers de ce répertoire, ou, le cas échéant, d'ouvrir tous les fichiers afin de s'assurer que toutes les occurrences du nom de fichier modifié ont elles-aussi été modifiées (les occurrences sont indiquées dans des commentaires dans les fichiers où elles se trouvent).

Le fichier du programme d'installation doit être exécutable (pas besoin de s'occuper des autres fichiers, l'installateur s'en charge tout seul).

### Installation et configuration

Une fois la copie terminée, il est possible d'installer tous les prérequis via la commande :

* Pour avoir l'installateur doté d'une interface affichable en console :

```BASH
sudo ./installateur.sh
```

* Pour avoir l'ancien installateur en texte :

```BASH
sudo ./ancien_installateur.sh # n'exécutez pas cette commande si la première a permis le lancement de l'installateur en TUI.
```

Ce programme se chargera automatiquement de :

* configurer le Wi-Fi (l'utilisateur peut choisir de configurer un Wi-Fi privé, *eduroam* ou de ne pas le configurer) ;
* installer toutes les bibliothèques Python requises pour le fonctionnement des scripts (dont `pyserial`, `requests`, `flask`, `sqlite3`, etc.) ;
* installer SQLite pour la gestion interne d'une mini base de données ;
* créer et configurer la mini base de donnée ;
* et si tout s'est bien passé :
  * configurer l'exécution automatique au démarrage du programme de relevé de mesures,
  * redémarrer le Raspberry Pi pour directement commencer l'exécution ;
* sinon :
  * indiquer les erreurs ayant eu lieu et terminer l'exécution du programme.

Le programme d'installation détecte automatiquement toute erreur lors de l'installation et annule la configuration automatique des scripts au démarrage en cas de problème.

Deux versions du programme installateur sont employables : 

* l'une d'entre elle est un installateur doté d'une interface conviviale – je pensais employer `dialog`, mais j'ai finalement utilisé `whiptail`, qui est plus léger et offre moins de possibilités, mais qui est parfait pour une utilisation sur Raspberry-Pi et que ne requiert, normalement, aucune installation de paquet supplémentaire ;
* l'autre est la version de l'installateur la plus ancienne et qui avait été développée en mode texte basique. Ce programme est également à jour et est toujours dans le repository dans l'hypothèse où l'interface du premier installatteur ne fonctionnerait pas. Il n'est toutefois pas recommandé de l'employer directement.

