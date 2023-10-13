import math

varNumber = int(input("Veuillez entrer le nombre de variable"))

valuationListe = []

for i in range(int(math.pow(2,varNumber))):#on va créer 2^varNumber ligne
    valuationListe.append([])
    for x in range(varNumber):#on remplie tout les valuation a 0 pour pouvoir les manipuler librement plus tard
        valuationListe[i].append(0)

suposedCount = 0.5
for i in range(varNumber):
    actualCount = 1
    suposedCount = suposedCount *2#on définit le nombre de 0 ou 1 qui se suivent comme 2 fois plus que précedemment
    zaped = True#variable servant a définir si on doit écrire des 1 ou des 0 (True = 0, False = 1)
    for x in range(len(valuationListe)): #pour chaque ligne
        if(actualCount <= suposedCount): #si jamais on a pas atteint le nombre de 1 ou 0 consécutif
            if(zaped == False):
                valuationListe[x][varNumber-i-1] = 1
            else:
                valuationListe[x][varNumber-i-1] = 0
            actualCount = actualCount + 1
        else: #si on a atteint le nombre de 1 ou 0 consécutif
            if zaped == True:
                zaped = False
            else:
                zaped = True
            actualCount = 1 #on va inverser la valeur qu'on écrit et reset le compteur de 1 ou 0 consécutif écrit 
            if(zaped == False):#et ensuite on va refaire une phase d'écriture
                valuationListe[x][varNumber-i-1] = 1
            else:
                valuationListe[x][varNumber-i-1] = 0
            actualCount = actualCount + 1

for i in range(len(valuationListe)):
    print(valuationListe[i])