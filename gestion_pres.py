import sqlite3
from core import affichage_resultat
from config import *

####################
# VARIABLE GLOBALE #
####################
CHOIX_DEFAUT = 2  # Retour AUTOMATIQUE sur l'écran 'Gestion des près' car nous sommes dans le module 'Gestion près'

##############################################################################################################
##############################################################################################################
# 					SECTION GESTION DE LA BASE DE DONNEES                                                    #
##############################################################################################################
##############################################################################################################

def lister_tous_pre() -> list:
    """
    Fonction permettant de lister tous les près de la table pre.
    
    Parameters:
    
    Returns:
    list: Une liste de dictionnaires, où chaque dictionnaire représente une ligne de résultat.
    """

    with sqlite3.connect(CHEMIN_BDD) as conn:
        cursor = conn.cursor()

        requete = """SELECT pre_id AS ID, nom AS NOM, capacite AS CAPACITE FROM pre
        ORDER BY 
            pre_id;"""

    cursor.execute(requete)

    # Récupérez les noms des colonnes
    nom_colonnes = [description[0] for description in cursor.description]

    # Créez une liste de dictionnaires, où chaque dictionnaire représente une ligne
    resultat = []
    for ligne in cursor.fetchall():
        resultat.append(dict(zip(nom_colonnes, ligne)))

    return resultat


        
def ajouter_pre(nom: str, capacite: int) -> None:
    """
    Fonction permettant d'ajouter un nouveau pré.
    
    Parameters:
    nom (str): Le nom du pré
    capacite (int) : capacite du pré
    
    Returns:
    """
    try:
        with sqlite3.connect(CHEMIN_BDD) as conn:
            cursor = conn.cursor()

            query = """
            INSERT INTO pre (nom, capacite)
            VALUES (?, ?)
            """

            cursor.execute(query, (nom, capacite))
            conn.commit()

        print(f"{GREEN}Le pré '{nom}' a été ajouté avec succès.{RESET}")

    except sqlite3.Error as e:
        print(f"{RED}Une erreur est survenue : {e}{RESET}")
        

def modifier_pre(pre_id: int, nom: str, capacite: int) -> None:
    """
    Fonction permettant de modifier les informations d'un pre par son id.
    
    Parameters:
    pre_id (int): Identifiant unique (clé primaire) du pre à modifier
    nom (str): Le nom du pre
    capacite (int) : la capacite du pre
    
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
            if capacite is not None:
                champs.append("capacite = ?")
                params.append(capacite)
            
            if not champs:
                print("{RED}Aucune modification spécifiée.{RESET}")
                return

            query = f"UPDATE pre SET {', '.join(champs)} WHERE pre_id = ?"
            params.append(pre_id)

            cursor.execute(query, params)

            if cursor.rowcount == 0:
                print(f"{RED}Aucun pre trouvé avec l'ID {pre_id}.{RESET}")
            else:
                conn.commit()
                print(
                    f"{GREEN}Le pre avec l'ID {pre_id} a été modifié avec succès.{RESET}"
                )

    except sqlite3.Error as e:
        print(f"{RED}Une erreur est survenue : {e}{RESET}")
        
def supprimer_pre(pre_id: int) -> None:
    """
    Fonction permettant de supprimer les informations d'un pré en base de données par son id.
    
    Parameters:
    pre_id (int): Identifiant unique (clé primaire) du pré à supprimer
    
    Returns:
    """
    try:
        with sqlite3.connect(CHEMIN_BDD) as conn:
            cursor = conn.cursor()
            query = "DELETE FROM pre WHERE pre_id = ?"
            cursor.execute(query, (pre_id,))

            if cursor.rowcount == 0:
                print(f"{RED}Aucun cheval trouvé avec l'ID {pre_id}.{RESET}")
            else:
                conn.commit()
                print(
                    f"{GREEN}Le pre avec l'ID {pre_id} a été supprimé avec succès.{RESET}"
                )

    except sqlite3.Error as e:
        print(f"{RED}Une erreur est survenue : {e}{RESET}")
        
##############################################################################################################
##############################################################################################################
# 					SECTION GESTION DES ECRANS                                                               #
##############################################################################################################
##############################################################################################################


def ecran_gestion_pres() -> int:
    print("\n#############################################")
    print("Ecran : Gestion des près")
    print("---------------------------")
    print("15-Lister tous les près")
    print("16-Ajouter un prè")
    print("17-Modifier les données d'un prè par son id")
    print("18-Supprimer la gestion d'un prè du centre par son id")
    print("")
    print("0-Retour à l'écran principal")
    choix = int(input("\n>Entrez votre choix :"))
    return choix

def ecran_liste_tous_pre() -> int:
    print("\n#############################################")
    print("Ecran : Lister tous les près")
    print("---------------------------")
    print("")
    resultat = lister_tous_pre()
    affichage_resultat(resultat)

    return CHOIX_DEFAUT

def ecran_ajouter_un_pre() -> int:
    print("\n#############################################")
    print("Ecran : Ajouter un cheval")
    print("---------------------------")
    print("")
    nom = input(">nom (TEXT) ?")
    capacite = int(input(">capacite (INTEGER) ?"))
    ajouter_pre(nom,capacite)

    return CHOIX_DEFAUT

def ecran_modifier_un_pre() -> int:
    print("\n#############################################")
    print("Ecran : Modifier les données d'un près")
    print("---------------------------")
    print("Liste des près :")
    resultat = lister_tous_pre()
    affichage_resultat(resultat)
    
    pre_id = None
    nom = None
    capacite = None
    

    try:
        pre_id = input(">pre_id (INTEGER) ?")
        nom = input(">nom (TEXT) ?")
        capacite = input(">capacite (INTEGER) ?")

        if pre_id == "":
            raise ValueError
        else:
            pre_id = int(pre_id)

        if nom == "":
            nom = None

        if capacite != "":
            capacite = int(capacite)
        else:
            capacite = None


    except ValueError as e:
        print(f"{RED}Une erreur est survenue : {e}{RESET}")
        print("")
        print("2-Retour à l'écran 'Gestion des près'")
        choix = int(input("\n>Entrez votre choix :"))
        return choix

    modifier_pre(pre_id, nom, capacite)

    return CHOIX_DEFAUT

def ecran_supprimer_un_pre() -> int:
    print("\n#############################################")
    print("Ecran : Supprimer les données d'un pre")
    print("---------------------------")
    print("")
    resultat = lister_tous_pre()
    affichage_resultat(resultat)
    print("")

    pre_id = None

    try:
        pre_id = input(">pre_id (INTEGER) ?")
        if pre_id == "":
            raise ValueError
        else:
            pre_id = int(pre_id)

    except ValueError as e:
        print(f"{RED}Une erreur est survenue : {e}{RESET}")
        print("")
        print("2-Retour à l'écran 'Gestion des pre'")
        choix = int(input("\n>Entrez votre choix :"))
        return choix

    supprimer_pre(pre_id)

    return CHOIX_DEFAUT