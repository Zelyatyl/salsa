import pytest
import sys
import os
import sqlite3

CHEMIN_BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHEMIN_TEST = CHEMIN_BASE + "\\src\\"

sys.path.append(CHEMIN_TEST)

from config import CHEMIN_BDD
from gestion_chevaux import lister_genre
from gestion_chevaux import lister_statut
from gestion_chevaux import lister_tous_chevaux
from gestion_chevaux import inserer_cheval


def test_lister_genre():
    resultat = lister_genre()
    assert len(resultat) == 2
    assert resultat[0] == {'genre_id': 1, 'genre': 'Hongre'}
    assert resultat[1] == {'genre_id': 2, 'genre': 'Jument'}


def test_lister_statut():
    resultat = lister_statut()
    assert len(resultat) == 2
    assert resultat[0] == {'statut_id': 1, 'etat': 'Actif'}
    assert resultat[1] == {'statut_id': 2, 'etat': 'En retraite'}


def test_lister_tous_chevaux():
    resultat = lister_tous_chevaux()
    assert len(resultat) == 18
    assert resultat[0] == {'ID': 1, 'NOM': "Écuyer d'Or", 'GENRE': 'Hongre', 'STATUT': 'Actif'}
    assert resultat[17] == {'ID': 18, 'NOM': "Douce Mélodie", 'GENRE': 'Jument', 'STATUT': 'Actif'}


def test_inserer_cheval():

    nom_test = "Cheval Test"
    genre_id_test = 1
    statut_id_test = 2
    
    inserer_cheval(nom_test, genre_id_test, statut_id_test)
    print(CHEMIN_BDD)
    with sqlite3.connect(CHEMIN_BDD) as conn:
        cursor = conn.cursor()
        requete = "SELECT * FROM cheval ORDER BY cheval_id DESC LIMIT 1;"

    cursor.execute(requete)
    nom_colonnes = [description[0] for description in cursor.description]
    resultat = []
    for ligne in cursor.fetchall():
        resultat.append(dict(zip(nom_colonnes, ligne)))
    
    assert len(resultat) == 1
    assert resultat[0]['nom'] == nom_test
    assert resultat[0]['genre_id'] == genre_id_test
    assert resultat[0]['statut_id'] == statut_id_test
    
    # Nettoyage
    id = resultat[0]['cheval_id']
    
    with sqlite3.connect(CHEMIN_BDD) as conn:
        cursor = conn.cursor()
        requete = "DELETE FROM cheval WHERE cheval_id=?;"
        cursor.execute(requete, (id,))
        conn.commit()
    

if __name__ == "__main__":
    pytest.main()