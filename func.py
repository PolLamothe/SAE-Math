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

def decalRight(array,index,value):
    result = []
    for i in range(len(array)):
        if i == index:
            result.append(value)
        result.append(array[i])
    return result