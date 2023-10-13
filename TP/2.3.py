import math

def h(x):
    if x >= 0:
        for i in range(0,x,7):
            print(i)

userInput = input("Entrez la valeur de x")
h(int(userInput))