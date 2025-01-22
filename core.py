import sqlite3
from config import *


def ecran_principal() -> int:
    print("\n#############################################")
    print("Ecran principal")
    print("---------------")
    print("1-Gestion des chevaux")
    print("2-Gestion des prés")
    print(f"\n{BLUE}90-Charger le schéma de la base{RESET}")
    print(f"{BLUE}91-Charger les données en base{RESET}")
    print(f"\n{RED}99-Arrêt du programme{RESET}")
    choix = int(input("\n>Entrez votre choix :"))
    return choix


def affichage_resultat(results: list) -> None:
    """
    Fonction permettant l'affichage d'une requète.
    
    Parameters:
    results (list): une liste de dictionnaires, où chaque dictionnaire représente une ligne d'une requête.
    
    Returns:
    """
        
    if not results:
        print(f"{RED}Aucun résultat à afficher.{RESET}")
        return

    # Obtenir les noms des colonnes
    columns = list(results[0].keys())

    # Afficher l'en-tête
    print(" | ".join(columns))
    print("_" * (sum(len(col) for col in columns) + 4 * (len(columns) - 1)))

    # Afficher les données
    for row in results:
        print(" | ".join(str(row[col]) for col in columns))


def executer_fichier_sql(chemin_fichier_sql: str) -> int:
    """
    Fonction permettant de charger un fichier SQL en base de données.
    """
    try:

        with open(chemin_fichier_sql, "r", encoding="utf-8") as file:
            script_sql = file.read()

        with sqlite3.connect(CHEMIN_BDD) as conn:
            cursor = conn.cursor()
            cursor.executescript(script_sql)
            conn.commit()

        print(f"{GREEN}Le fichier SQL a été exécuté avec succès.{RESET}")
        print("")
        print("")
        print("0-Retour à l'écran principal")
        choix = int(input("\n>Entrez votre choix :"))
        return choix

    except sqlite3.Error as e:
        print(f"{RED}Une erreur SQLite s'est produite : {e}{RESET}")

    except IOError as e:
        print(
            f"{RED}Une erreur lors de la lecture du fichier s'est produite : {e}{RESET}"
        )


def charger_schema() -> int:
    """
    Fonction permettant de charger le schéma intégral de la base de données.
    """
    return executer_fichier_sql(CHEMIN_SCHEMA)


def charger_donnees() -> int:
    """
    Fonction permettant de charger les données de la base de données.
    """
    return executer_fichier_sql(CHEMIN_DATA)
