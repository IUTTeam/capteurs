echo "     ____                            _______                     __ "
echo "    / __ \             _      __    /__  __/     __             /_/ "
echo "   / /_/ /________    (_)__  / /_     / / __  __/ /_____  ________  "
echo "  / ____/ ___/ __ \  / / _ \/ __/    / / / / / / __/ __ \/ ___/ _ \ "
echo " / /   / /  / /_/ / / /  __/ /_     / / / /_/ / /_/ /_/ / /  /  __/ "
echo "/_/   /_/   \____/ / /\___/\__/    /_/  \__,_/\__/\____/_/   \___/  "
echo "           _______/ /                                               "
echo "          / _______/        __                                      "
echo "         / /   ____ _____  / /____  __  ____________                "
# échappement d'un caractère, le texte n'est pas décalé à l'affichage :
echo "        / /   / __ \`/ __ \/ __/ _ \/ / / / ___/ ___/                "
echo "       / /___/ /_/ / /_/ / /_/  __/ /_/ / /  (__  )                 "
echo "       \____/\__,_/ .___/\__/\___/\__,_/_/  /____/                  "
echo "                 / /                                                "
echo "                /_/      Lancement du script sur le Rapsberry Pi.   "
echo "                                                                    "

# on pourrait aussi changer le fichier motd…

python3 /projetTut/acquisition_donnees.py

# Attention ! Le nom de ce fichier apparait dans le programme d'installation.
# Ce fichier permet le changement du path et du nom de /projetTut/acquisition_donnees.py
# sans avoir besoin de tout réinstaller dans le fichier init.d
