import os
from config import *
import core
import gestion_chevaux
import gestion_pres


####################
# VARIABLE GLOBALE #
####################

# Ajouter ici les ecrans avec une clé unique
switch_dict = {
    0: core.ecran_principal,
    1: gestion_chevaux.ecran_gestion_chevaux,
    11: gestion_chevaux.ecran_liste_tous_chevaux,
    12: gestion_chevaux.ecran_ajouter_un_cheval,
    13: gestion_chevaux.ecran_modifier_un_cheval,
    14: gestion_chevaux.ecran_supprimer_un_cheval,
    2: gestion_pres.ecran_gestion_pres,
    15: gestion_pres.ecran_liste_tous_pre,
    16: gestion_pres.ecran_ajouter_un_pre,
    17: gestion_pres.ecran_modifier_un_pre,
    18: gestion_pres.ecran_supprimer_un_pre,
    90: core.charger_schema,
    91: core.charger_donnees,
}


##############################################################################################################
##############################################################################################################
# 					PROGRAMME PRINCIPAL					                                                     #
##############################################################################################################
##############################################################################################################


def fichier_existe(chemin_fichier: str) -> bool:
    """
    Contrôle l'existance d'un fichier à partir d'un chemin.
    
    Parameters:
    chemin_fichier (str): Le chemin du fichier à tester.
    
    Returns:
    bool: Renvoie True si le fichier existe, False sinon.
    """
    try:
        with open(chemin_fichier) as file:
            print(f"Contrôle : '{chemin_fichier}' {GREEN}OK{RESET}")
            return True
    except FileNotFoundError as e:
        print(f"{RED}Le fichier n'a pas été trouvé : {e}{RESET}")
    return False


def inconnu() -> str:
    """
    Renvoie la chaine une chaine de caractère "INCONNU".
    Cas où switch_dict ne reconnait pas l'identifiant envoyé.
    """
    return "INCONNU"


def routage(identifiant_ecran: int) -> ():
    """
    Appel la fonction d'affichage adéquate en fonction de son identifiant.
    @switch_dict
    """
    return switch_dict.get(identifiant_ecran, inconnu)()


if __name__ == "__main__":

    os.system("mode con: cols=200 lines=70")
    print(
        f"{BLUE}##################################################################################{RESET}"
    )
    print(f"{BLUE}                        GESTION CENTRE EQUESTRE{RESET}")
    print(
        f"{BLUE}##################################################################################{RESET}"
    )

    fichier_existe(CHEMIN_BDD)
    fichier_existe(CHEMIN_SCHEMA)
    fichier_existe(CHEMIN_DATA)

    execution = True
    choix = 0

    while execution:
        choix = routage(choix)

        if choix == "INCONNU":
            print(
                f"{RED}Il y a une erreur dans la saisie de votre choix. Retour à l'écran principal.{RESET}"
            )
            choix = 0
        if choix == 99:
            choix_quitter = input(
                f"\n{BLUE}>Voulez-vous vraiment quitter l'application ? [OUI/NON]{RESET}"
            )
            if choix_quitter == "OUI" or "O":
                execution = False
            elif choix_quitter == "NON" or "N":
                print(f"{BLUE}Retour à l'écran principal.{RESET}")
                choix = 0

    exit(0)
