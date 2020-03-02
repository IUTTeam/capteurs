# capteurs

> Pensez à lire la documentation en entier, ça peut toujours servir (RTFM).

## Script d'acquisition des données

Acquisition des données via un Arduino et un Raspberry Pi

Il faut installer `pyserial` pour communiquer avec l'Arduino :
```BASH
pip3 install pyserial
```

## Programme d'installation

### Copie des fichiers sur le Raspberry-Pi

Tous les fichiers contenu dans ce répertoire sont à copier sur le Rapsberry-Pi dans `/ProjetTut`.

Il est nécessaire de ne pas changer les noms des fichiers de ce répertoire, ou, le cas échéant, d'ouvrir tous les fichiers afin de s'assurer que toutes les occurrences du nom de fichier modifié ont elles-aussi été modifiées (les occurrences sont indiquées dans des commentaires dans les fichiers où elles se trouvent).

Le fichier du programme d'installation doit être exécutable (pas besoin de s'occuper des autres fichiers, l'installateur s'en charge tout seul).

### Installation et configuration

Une fois la copie terminée, il est possible d'installer tous les prérequis via la commande :

```BASH
sudo ./programmeInstallateur.sh
```

Ce programme se chargera automatiquement de :

* configurer le Wi-Fi (l'utilisateur peut choisir de configurer un Wi-Fi privé, *eduroam* ou de ne pas le configurer) ;
* installer toutes les bibliothèques Python requises pour le fonctionnement des scripts (dont `pyserial`, `requests`, `sqlite3`, etc.) ;
* installer SQLite pour la gestion interne d'une mini base de données ;
* créer et configurer la mini base de donnée ;
* et si tout s'est bien passé, configurer l'exécution automatique au démarrage du programme de relevé de mesures.

Le programme d'installation détecte automatiquement toute erreur lors de l'installation et annule la configuration automatique des scripts au démarrage en cas de problème.

Pour l'instant, l'interface du programme d'installation est moche et est en texte, mais :

1. on s'en fout ;
2. je ne pense pas que la commande BASH « `dialog` » est installée par défaut sur le Raspberry-Pi.  
→ En revanche, pour un programme de configuration a destination de l'utilisateur final, ce serait intéressant de mettre ça en place. À voir.