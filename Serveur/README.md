Pour la réception des données, envoyer au serveur à l'url : NOM_SITE/send_to_server et au port : 1234 (temporaire)

...une méthode POST dont le body contient un JSON du format suivant :
{
	"type":NOM_TYPE,
	"donnees":[
		[VALEUR_DONNEE_1, TIMESTAMP_PRISE_DONNEE_1],
		[VALEUR_DONNEE_1, TIMESTAMP_PRISE_DONNEE_2],
		...
		[VALEUR_DONNEE_N, TIMESTAMP_PRISE_DONNEE_N]
	]
}

Les timestamps sont des timestamps UNIX classiques (càd nombre de secondes depuis 1er Janvier 1970)
Pour le moment, une seul requête par type de données que l'on souhaite envoyer, si cela pose des contraintes à voir pour modifier l'architecture du JSON...