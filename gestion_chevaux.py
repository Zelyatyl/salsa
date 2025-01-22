import sqlite3
from core import affichage_resultat
from config import *

####################
# VARIABLE GLOBALE #
####################
CHOIX_DEFAUT = 1  # Retour AUTOMATIQUE sur l'écran 'Gestion des chevaux' car nous sommes dans le module 'Gestion chevaux'

##############################################################################################################
##############################################################################################################
# 					SECTION GESTION DE LA BASE DE DONNEES                                                    #
##############################################################################################################
##############################################################################################################


def lister_tous_chevaux() -> list:
    """
    Fonction permettant de lister tous les chevaux de la table cheval.
    
    Parameters:
    
    Returns:
    list: Une liste de dictionnaires, où chaque dictionnaire représente une ligne de résultat.
    """

    with sqlite3.connect(CHEMIN_BDD) as conn:
        cursor = conn.cursor()

        requete = """SELECT cheval_id AS ID, nom AS NOM, genre AS GENRE, etat AS STATUT FROM cheval
        INNER JOIN 
            genre ON genre.genre_id = cheval.genre_id
        INNER JOIN 
            statut ON statut.statut_id = cheval.statut_id
        ORDER BY 
            cheval_id;"""

    cursor.execute(requete)

    # Récupérez les noms des colonnes
    nom_colonnes = [description[0] for description in cursor.description]

    # Créez une liste de dictionnaires, où chaque dictionnaire représente une ligne
    resultat = []
    for ligne in cursor.fetchall():
        resultat.append(dict(zip(nom_colonnes, ligne)))

    return resultat


def lister_genre() -> list:
    """
    Fonction permettant de lister tous les genres de la table genre.
    
    Parameters:
    
    Returns:
    list: Une liste de dictionnaires, où chaque dictionnaire représente une ligne de résultat.
    """
    with sqlite3.connect(CHEMIN_BDD) as conn:
        cursor = conn.cursor()

        requete = "SELECT * FROM genre;"

    cursor.execute(requete)
    nom_colonnes = [description[0] for description in cursor.description]
    resultat = []
    for ligne in cursor.fetchall():
        resultat.append(dict(zip(nom_colonnes, ligne)))

    return resultat


def lister_statut() -> list:
    """
    Fonction permettant de lister tous les statuts de la table statut.
    
    Parameters:
    
    Returns:
    list: Une liste de dictionnaires, où chaque dictionnaire représente une ligne de résultat.
    """
    with sqlite3.connect(CHEMIN_BDD) as conn:
        cursor = conn.cursor()

        requete = "SELECT * FROM statut;"

    cursor.execute(requete)
    nom_colonnes = [description[0] for description in cursor.description]
    resultat = []
    for ligne in cursor.fetchall():
        resultat.append(dict(zip(nom_colonnes, ligne)))

    return resultat


def inserer_cheval(nom: str, genre_id: int, statut_id: int) -> None:
    """
    Fonction permettant d'inserer un nouveau cheval.
    
    Parameters:
    nom (str): Le nom du cheval
    genre_id (int) : Clé étrangère genre_id de la table genre
    statut_id (int) : Clé étrangère statut_id de la table statut
    
    Returns:
    """
    try:
        with sqlite3.connect(CHEMIN_BDD) as conn:
            cursor = conn.cursor()

            query = """
            INSERT INTO cheval (nom, genre_id, statut_id)
            VALUES (?, ?, ?)
            """

            cursor.execute(query, (nom, genre_id, statut_id))
            conn.commit()

        print(f"{GREEN}Le cheval '{nom}' a été inséré avec succès.{RESET}")

    except sqlite3.Error as e:
        print(f"{RED}Une erreur est survenue : {e}{RESET}")


def modifier_cheval(cheval_id: int, nom: str, genre_id: int, statut_id: int) -> None:
    """
    Fonction permettant de modifier les informations d'un cheval par son id.
    
    Parameters:
    cheval_id (int): Identifiant unique (clé primaire) du chaval à modifier
    nom (str): Le nom du cheval
    genre_id (int) : Clé étrangère genre_id de la table genre
    statut_id (int) : Clé étrangère statut_id de la table statut
    
    Returns:
    """
    try:
        with sqlite3.connect(CHEMIN_BDD) as conn:
            cursor = conn.cursor()

            champs = []
            params = []

            if nom is not None:
                champs.append("nom = ?")
                params.append(nom)
            if genre_id is not None:
                champs.append("genre_id = ?")
                params.append(genre_id)
            if statut_id is not None:
                champs.append("statut_id = ?")
                params.append(statut_id)

            if not champs:
                print("{RED}Aucune modification spécifiée.{RESET}")
                return

            query = f"UPDATE cheval SET {', '.join(champs)} WHERE cheval_id = ?"
            params.append(cheval_id)

            cursor.execute(query, params)

            if cursor.rowcount == 0:
                print(f"{RED}Aucun cheval trouvé avec l'ID {cheval_id}.{RESET}")
            else:
                conn.commit()
                print(
                    f"{GREEN}Le cheval avec l'ID {cheval_id} a été modifié avec succès.{RESET}"
                )

    except sqlite3.Error as e:
        print(f"{RED}Une erreur est survenue : {e}{RESET}")


def supprimer_cheval(cheval_id: int) -> None:
    """
    Fonction permettant de supprimer les informations d'un cheval en base de données par son id.
    
    Parameters:
    cheval_id (int): Identifiant unique (clé primaire) du cheval à supprimer
    
    Returns:
    """
    try:
        with sqlite3.connect(CHEMIN_BDD) as conn:
            cursor = conn.cursor()
            query = "DELETE FROM cheval WHERE cheval_id = ?"
            cursor.execute(query, (cheval_id,))

            if cursor.rowcount == 0:
                print(f"{RED}Aucun cheval trouvé avec l'ID {cheval_id}.{RESET}")
            else:
                conn.commit()
                print(
                    f"{GREEN}Le cheval avec l'ID {cheval_id} a été supprimé avec succès.{RESET}"
                )

    except sqlite3.Error as e:
        print(f"{RED}Une erreur est survenue : {e}{RESET}")


##############################################################################################################
##############################################################################################################
# 					SECTION GESTION DES ECRANS                                                               #
##############################################################################################################
##############################################################################################################


def ecran_gestion_chevaux() -> int:
    print("\n#############################################")
    print("Ecran : Gestion des chevaux")
    print("---------------------------")
    print("11-Lister tous les chevaux")
    print("12-Ajouter un cheval")
    print("13-Modifier les données d'un cheval par son id")
    print("14-Supprimer la gestion d'un cheval du centre par son id")
    print("")
    print("0-Retour à l'écran principal")
    choix = int(input("\n>Entrez votre choix :"))
    return choix


def ecran_liste_tous_chevaux() -> int:
    print("\n#############################################")
    print("Ecran : Lister tous les chevaux")
    print("---------------------------")
    print("")
    resultat = lister_tous_chevaux()
    affichage_resultat(resultat)

    return CHOIX_DEFAUT


def ecran_ajouter_un_cheval() -> int:
    print("\n#############################################")
    print("Ecran : Ajouter un cheval")
    print("---------------------------")
    print("")
    print("Genre :")
    liste_genres = lister_genre()
    affichage_resultat(liste_genres)
    print("--------")
    print("Statut :")
    liste_statuts = lister_statut()
    affichage_resultat(liste_statuts)
    print("--------")

    nom = input(">nom (TEXT) ?")
    genre_id = int(input(">genre_id (INTEGER) ?"))
    statut_id = int(input(">statut_id INTEGER ?"))
    inserer_cheval(nom, genre_id, statut_id)

    return CHOIX_DEFAUT


def ecran_modifier_un_cheval() -> int:
    print("\n#############################################")
    print("Ecran : Modifier les données d'un cheval")
    print("---------------------------")
    print("Liste des chevaux :")
    resultat = lister_tous_chevaux()
    affichage_resultat(resultat)
    print("--------")
    print("Genre :")
    liste_genres = lister_genre()
    affichage_resultat(liste_genres)
    print("--------")
    print("Statut :")
    liste_statuts = lister_statut()
    affichage_resultat(liste_statuts)
    print("--------")

    cheval_id = None
    nom = None
    genre_id = None
    statut_id = None

    try:
        cheval_id = input(">cheval_id (INTEGER) ?")
        nom = input(">nom (TEXT) ?")
        genre_id = input(">genre_id (INTEGER) ?")
        statut_id = input(">statut_id (INTEGER) ?")

        if cheval_id == "":
            raise ValueError
        else:
            cheval_id = int(cheval_id)

        if nom == "":
            nom = None

        if genre_id != "":
            genre_id = int(genre_id)
        else:
            genre_id = None

        if statut_id != "":
            statut_id = int(statut_id)
        else:
            statut_id = None

    except ValueError as e:
        print(f"{RED}Une erreur est survenue : {e}{RESET}")
        print("")
        print("1-Retour à l'écran 'Gestion des chevaux'")
        choix = int(input("\n>Entrez votre choix :"))
        return choix

    modifier_cheval(cheval_id, nom, genre_id, statut_id)

    return CHOIX_DEFAUT


def ecran_supprimer_un_cheval() -> int:
    print("\n#############################################")
    print("Ecran : Supprimer les données d'un cheval")
    print("---------------------------")
    print("")
    resultat = lister_tous_chevaux()
    affichage_resultat(resultat)
    print("")

    cheval_id = None

    try:
        cheval_id = input(">cheval_id (INTEGER) ?")
        if cheval_id == "":
            raise ValueError
        else:
            cheval_id = int(cheval_id)

    except ValueError as e:
        print(f"{RED}Une erreur est survenue : {e}{RESET}")
        print("")
        print("1-Retour à l'écran 'Gestion des chevaux'")
        choix = int(input("\n>Entrez votre choix :"))
        return choix

    supprimer_cheval(cheval_id)

    return CHOIX_DEFAUT
