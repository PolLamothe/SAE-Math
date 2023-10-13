def est_ensemble(l):
    verifiedListe = []
    for i in l:
        tempCounter = 0
        for x in range(len(verifiedListe)+1): #on ajoute 1 dans la boucle au cas ou la liste soit vide au début du programme
            try: #on met try pour ne pas que le programme crash en essayant d'accéder a verifiedListe[len(verifiedListe)+1] car on a ajouté 1 dans la boucle
                if(verifiedListe[x] != i): #on augmente tempcounter si l'élément actuel de l n'es pas l'élément actuel de verifiedListe
                    tempCounter = tempCounter + 1
            except:
                tempCounter = tempCounter
        if(tempCounter == len(verifiedListe)): #si jamais aucun des éléments de verifiedListe n'est égale a l
            verifiedListe.append(i) 
    if(len(verifiedListe) == len(l)): #si jamais il y'a eu autant d'élément de l validé comme unique que d'élément dans l
        return True
    else :
        return False
    
def suppr_doublons(l):
    verifiedListe = []
    for i in l:
        tempCounter = 0
        for x in range(len(verifiedListe)+1):
            try:
                if(verifiedListe[x] != i):
                    tempCounter = tempCounter + 1
            except:
                tempCounter = tempCounter
        if(tempCounter == len(verifiedListe)):
            verifiedListe.append(i)
    return verifiedListe #on retourne verifiedListe car c'est une liste où si jamais l'élément de l actuelle y était déja présent il n'y était pas ajouté

import unittest

