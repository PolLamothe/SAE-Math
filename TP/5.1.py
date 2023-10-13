import math

Ensemble = set({"Pol","Baptiste","Paul émile","Mathieu"})
EnsembleInt = set({1,5,26,38})

def affiche_col(E):
    for i in E:
        print(i)

def membre(x,E):
    for i in E:
        if(x == i):
            return True
    return False

def somme(E):
    sum = 0
    for i in E:
        try:#on essaie de transformer l'élément actuelle en un int au cas ou il soit stocké sous un string et si ça échoue en revoie False
            sum = sum + int(i)
        except:
            return False
    return sum

def taille(E):
    counter = 0
    for i in E:
        counter = counter+1
    return counter