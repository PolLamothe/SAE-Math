import math

def carres(liste):
    newListe = []
    for i in liste:
        newListe.append(i*i)
    return newListe

liste = [1,2,8,3,11,2,5,32,1]

print("voici la liste : "+str(liste))

print("voici le résultat de la fonction : "+str(carres(liste)))