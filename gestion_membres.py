import sqlite3
from core import affichage_resultat
from config import *

####################
# VARIABLE GLOBALE #
####################
CHOIX_DEFAUT = 1  # Retour AUTOMATIQUE sur l'écran 'Gestion des Membres' car nous sommes dans le module 'Gestion Membres'

##############################################################################################################
##############################################################################################################
# 					SECTION GESTION DE LA BASE DE DONNEES                                                    #
##############################################################################################################
##############################################################################################################

def authentification():
    identifiant = input("Entrez votre identifiant : ")
    mot_de_passe = input("Entrez votre mot de passe : ")
    
    # Vérification de l'identifiant et du mot de passe
    cursor.execute("""
        SELECT m.membre_id, m.identifiant, r.role
        FROM membre m
        JOIN role r ON m.role_id = r.role_id
        WHERE m.identifiant = ? AND m.mot_de_passe = ?
    """, (identifiant, mot_de_passe))
    user = cursor.fetchone()
    
    if user:
        membre_id, identifiant, role = user
        print(f"Authentification réussie ! Bienvenue {identifiant}.")
        print(f"Votre rôle est : {role}")
        
        if role == "Adhérent":
            ecran_adherent()
        elif role == "Propriétaire":
            ecran_proprietaire()
        elif role == "Gestionnaire":
            ecran_gestionnaire()
    else:
        print("Identifiant ou mot de passe incorrect. Veuillez réessayer.")

# Fonctions pour chaque écran
def ecran_adherent():
    print("Écran réservé aux adhérents.")

def ecran_proprietaire():
    print("Écran réservé aux propriétaires.")

def ecran_gestionnaire():
    print("Écran réservé aux gestionnaires.")





