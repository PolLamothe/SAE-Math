import math
from porteLogique import * #les fonctions des portes logiques se trouve dans le fichier porteLogique.py

def getUserVaraible(name):
    return int(input("Veuillez rentrer la valeur de "+ name+ " (0 ou 1) \n"))

def ShowResult(result):
    print("le résultat de votre opération est : "+ str(result))

while True:
    print("Voici la liste des opérateurs : \n 1-ET(x,y) \n 2-OU(x,y) \n 3-NON(x) \n 4-IMPLIQUE(x,y)\n")
    userChoice = input("Veuillez entrez les opérations \n")
    userChoice = "print("+ userChoice + ")"
    exec(userChoice)
