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
    let retour = await fonctionUtilisee(requete);
    reponse.statusCode = retour.codeReponse;
    reponse.setHeader('Content-type', 'text/plain');
    reponse.end(retour.reponse);
}

let envoyerDonneeAuServeur = async function(requete) {
	let reponse = null;
	let codeReponse = null;

	let mauvaiseRequete = false;

	const connexionSQL = getConnexionSQL();

    if (requete.method === "POST") {
    	let donneesPost = '';
    	requete.on('data', function(partie) {
        	donneesPost += partie.toString();

    	});
    	requete.on('end', await async function() {
    		try {
	    		donneesPost = JSON.parse(donneesPost);
	    		let type = donneesPost.type;
	    		let donnees = donneesPost.donnees;
		        const typeExiste = await typeDAO.typeExiste(connexionSQL, type);
		        if (!typeExiste) {
		        	await typeDAO.ajouterType(connexionSQL, type);
		        }
	    		for (let i = 0;i<donnees.length;i++) {
	    			let valeurCourante = donnees[i][0];
	    			let dateCourante = donnees[i][1];
	    			await donneesDAO.ajouterDonnee(connexionSQL, type, valeur, date);
	    		}
	    		reponse = "OK";
	    		codeReponse = consts.CODE_REPONSE_CORRECT;
    		}
    		catch (error) {
    			console.log("ERREUR");
    			mauvaiseRequete = true;
    		}
    	});
    }
    else {
    	console.log(requete.method);
    	mauvaiseRequete = true;
    }

	if (mauvaiseRequete) {
		reponse = consts.ERREUR_PREFIXE + consts.ERREUR_REQUETE_INCORRECT;
		codeReponse = consts.CODE_REPONSE_MAUVAISE_REQUETE;
	}
	return {
		"reponse" : reponse,
		"codeReponse" : codeReponse,
	}
}

let recevoirDonneeDeServeur = async function(requete) {
	let reponse = null;
	let codeReponse = null;

	const connexionSQL = getConnexionSQL();

	return {
		"reponse" : reponse,
		"codeReponse" : codeReponse,
	}	
}

let requeteParDefaut = function(requete) {
	return {
		"reponse" : consts.RETOUR_PAGE_ACCUEIL,
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