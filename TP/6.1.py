def inclus(A,B):
    scannedElement = []
    counter = 0
    ASize = 0
    for i in A:
        ASize = ASize+1
        for x in B:
            if(i == x):
                counter2 = 0
                for y in scannedElement:
                    if(y != i):
                        counter2 = counter2+1
                if(counter2 == len(scannedElement)):
                    counter = counter + 1
                    scannedElement.append(i)
    if(ASize == counter):
        return True
    else : 
        return False

def egal(A,B):
    counter = 0
    counter2 = 0
    for i in A:
        for x in B:
            if i == x:
                counter = counter + 1
    for i in B:
        for x in A:
            if i == x:
                counter2 = counter2 + 1
    if counter == len(A) and counter2 == len(B):
        return True
    else:
        return False

def disjoint(A,B):
    for i in A:
        for x in B:
            if i == x:
                return False
    return True

import unittest

class TestInclus(unittest.TestCase):
    def test_(self):
        A = set({"Pol"})
        B = set({"Pol","Mathieu"})
        self.assertEqual(inclus(A,B),True)

    def test_False(self):
        A = set({"Baptiste"})
        B = set({"Pol","Mathieu"})
        self.assertEqual(inclus(A,B),False)

class TestEgal(unittest.TestCase):
    def test_Egal(self):
        A = set({"Pol","Mathieu"})
        B = set({"Pol","Mathieu"})
        self.assertEqual(egal(A,B),True)
    def test_notEgal(self):
        A = set({"Baptiste","Théo"})
        B = set({"Pol","Mathieu"})
        self.assertEqual(egal(A,B),False)

class TestDisjoint(unittest.TestCase):
    def test_Disjoint(self):
        A = set({"Baptiste","Théo"})
        B = set({"Pol","Mathieu"})
        self.assertEqual(disjoint(A,B),True)
    def test_PasDisjoint(self):
        A = set({"Baptiste","Théo"})
        B = set({"Pol","Baptiste"})
        self.assertEqual(disjoint(A,B),False)



if __name__ == '__main__':
    unittest.main()