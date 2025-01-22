import os

os.system("")

RED = "\033[91m"
GREEN = "\033[92m"
BLUE = "\033[94m"
RESET = "\033[0m"

CHEMIN_BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHEMIN_BDD = CHEMIN_BASE + "\\bdd\\" + "centreEquestre.db"
CHEMIN_SCHEMA = CHEMIN_BASE + "\\bdd\\" + "schema.sql"
CHEMIN_DATA = CHEMIN_BASE + "\\bdd\\" + "data.sql"
