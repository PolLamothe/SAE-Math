def ET(x,y):
    if(x == True):
        if(y == True):
            return True
    return False

def OU(x,y):
    if(x == True):
        return True
    if(y == True):
        return True
    return False

def NON(x):
    if(x == True):
        return False
    else:
        return True
    
def IMPLIQUE(x,y):
    if(x == False):
        return True
    if(y == True):
        return True
    return  False