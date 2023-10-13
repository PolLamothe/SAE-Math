import math

def g(x):
    if x < 0:
        return math.sqrt(-x)
    else:
        return math.sqrt(x)

userInput = input("Entrez le parametre")

print(g(int(userInput)))