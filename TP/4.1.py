import math
from porteLogique import * #les fonctions des portes logiques se trouve dans le fichier porteLogique.py

while True:
    print("Voici la liste des opérateurs : \n 1-ET(x,y) \n 2-OU(x,y) \n 3-NON(x) \n 4-IMPLIQUE(x,y)\n")
    userChoice = input("Veuillez entrez les opérations \n")
    userChoice = "print("+ userChoice + ")"
    exec(userChoice)
