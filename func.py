def isInArray(array,item):
    for i in array:
        if i == item:
            return True
    return False

def removeFromArray(array,item):
    result = []
    for i in array:
        if i != item:
            result.append(i)
    return result