import math
from porteLogique import *
import json

p=-1
q=-1
r=-1

def F1(p,q,r) :
    return IMPLIQUE(NON(p),ET(q,r))
def F2(p,q,r):
    return IMPLIQUE(q,ET(NON(p),NON(r)))

paramsListe = []
resultListe = []

print("  p q r   ET(F1,F2)")
for i in range(2):
    p = p+1
    for i in range(2):
        q = q + 1
        for i in range(2):
            r = r + 1
            paramsListe.append("p:" + str(p)+",q:" + str(q)+",r:" +str(r))#j'ajoute a la liste des variables le nom de la variable et sa valeur
            resultListe.append(ET(F1(p,q,r),F2(p,q,r)))#j'ajoute a la liste des résultat, le résultat correspondant aux valeurs des variables du même index dans la liste des paramêtre
            print({str(p)+ " "+str(q) +" "+str(r): ET(F1(p,q,r),F2(p,q,r))})
        r = -1
    q = -1
    
result = zip(paramsListe,resultListe)
print(set(result))
