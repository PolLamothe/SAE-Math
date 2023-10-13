def ET(x,y):
    x = int(x)
    y = int(y)
    if(x == 1):
        if(y == 1):
            return 1
    return 0

def OU(x,y):
    x = int(x)
    y = int(y)
    if(x == 1):
        return 1
    if(y == 1):
        return 1
    return 0

def NON(x):
    x = int(x)
    if(x == 1):
        return 0
    else:
        return 1
    
def IMPLIQUE(x,y):
    x = int(x)
    y = int(y)
    if(x == 0):
        return 1
    if(y == 1):
        return 1
    return  0