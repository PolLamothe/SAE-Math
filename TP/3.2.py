import math

def compte(el, liste):
    counter = 0
    for i in liste:
        if(i == el):
            counter += 1
    return counter

liste = [4,5,7,4,4,5,3,6,8,7,4]

el = 4

print("voici la liste : "+ str(liste))

el = input("Entre le nombre dont vous voulez connaitre le nombre d'apparition dans la liste : ")

print("Voici le résultat de la fonction : "+str(compte(int(el),liste)))