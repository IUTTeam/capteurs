const http = require('http');
const mysql = require('mysql');
const util = require('util');
const URL = require('url').URL;
const donneesDAO = require('./DonneeDAO');
const typeDAO = require('./TypeDAO');
const consts = require('./Consts');

let traiteurRequetes = async function(requete,reponse)
{
	let txtReponse = "";
	let codeReponse = 200;
	const requeteURL = new URL(consts.PROTOCOLE + requete.headers.host + requete.url);
	let fonctionUtilisee = null;
    switch (requeteURL.pathname) {
    	case consts.URL_ENVOYER_SERVEUR:
    		fonctionUtilisee = envoyerDonneeAuServeur;
    		break;
        case consts.URL_RECEVOIR_SERVEUR:
        	fonctionUtilisee = recevoirDonneeDeServeur;
        	break;
        default:
        	fonctionUtilisee = requeteParDefaut;
        	break;
    }
    let retour = await fonctionUtilisee(requeteURL);
    reponse.statusCode = retour.codeReponse;
    reponse.setHeader('Content-type', 'text/plain');
    reponse.end(retour.json);
}

let envoyerDonneeAuServeur = async function(requeteURL) {
	let json = null;
	let codeReponse = null;

	const connexionSQL = getConnexionSQL();

    let type = requeteURL.searchParams.get(consts.REQUETE_CLE_TYPE);
    let valeur = requeteURL.searchParams.get(consts.REQUETE_CLE_DATE);
    let date = requeteURL.searchParams.get(consts.REQUETE_CLE_VALEUR);

    let estOK = type !== null && valeur !== null && date !== null;

	if (estOK) {
        const typeExiste = await typeDAO.typeExiste(connexionSQL, type);
        if (!typeExiste) {
        	await typeDAO.ajouterType(connexionSQL, type);
        }
        json = await donneesDAO.ajouterDonnee(connexionSQL, type, valeur, date);
        codeReponse = consts.CODE_REPONSE_CORRECT;
	}
	else {
		json = consts.ERREUR_PREFIXE + consts.ERREUR_FORMAT_REQUETE_INCORRECT;
		codeReponse = consts.CODE_REPONSE_MAUVAISE_REQUETE;
	}
	return {
		"json" : json,
		"codeReponse" : codeReponse,
	}
}

let recevoirDonneeDeServeur = async function(requeteURL) {
	let json = null;
	let codeReponse = null;

	const connexionSQL = getConnexionSQL();

	return {
		"json" : json,
		"codeReponse" : codeReponse,
	}	
}

let requeteParDefaut = function(requeteURL) {
	return {
		"json" : consts.RETOUR_PAGE_ACCUEIL,
		"codeReponse" : consts.CODE_REPONSE_CORRECT,
	}
}

let getConnexionSQL = function() {
	const pool = mysql.createPool({
	  connectionLimit: consts.LIMITE_CONNEXIONS_SIMULTANNEES,
	  host: consts.HOTE,
	  user: consts.UTILISATEUR_BASE_DE_DONNEES,
	  password: consts.MOT_DE_PASSE_BASE_DE_DONNEES,
	  database: consts.BASE_DE_DONNEES,
	})

	// Ping database to check for common exception errors.
	pool.getConnection((err, connection) => {
	  if (err) {
	    if (err.code === consts.ERREUR_CONNEXION_PERDUE) {
	      console.log(consts.ERREUR_PREFIXE + CODE_ERREUR_CONNEXION_PERDUE);
	    }
	    if (err.code === consts.ERREUR_SURPLUS_CONNEXION) {
	      console.log(consts.ERREUR_PREFIXE + CODE_ERREUR_SURPLUS_CONNEXION);
	    }
	    if (err.code === consts.ERREUR_CONNEXION_REFUSEE) {
	      console.log(consts.ERREUR_PREFIXE + CODE_ERREUR_CONNEXION_REFUSEE);
	    }
	  }

	  if (connection) {
		connection.release();
	  }
	});

	pool.query = util.promisify(pool.query);
	return pool;
}

let serveur = http.createServer(traiteurRequetes);
serveur.listen(consts.PORT, consts.HOTE, function() {
	console.log(consts.RETOUR_SERVEUR_OPERATIONNEL);
});