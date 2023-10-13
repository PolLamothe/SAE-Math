def ajout(x,E):
    E.add(x)
    return E

def union(A,B):
    result = set({})
    for i in A:
        result = ajout(i,result)
    for i in B:
        result = ajout(i,result)
    return result

def intersection(A,B):
    result = set({})
    for i in A:
        for x in B:
            if i == x:
                result = ajout(i,result)
    return result

def retire(x,E):
    result = set({})
    for i in E:
        if i != x:
            result = ajout(i,result)
    return result

def diff(A,B):
    result = set({})
    for i in A:
        counter = 0
        for x in B:
            if i != x:
                counter = counter + 1
        if counter == len(B):
            result = ajout(i,result)
    return result

def combiner(A,B):
    result = set({})
    for i in A:
        result = ajout(i,result)
    for i in B:
        result = ajout(i,result)
    return result

def diff_sym(A,B):
    AFiltred = diff(A,B)
    BFiltred = diff(B,A)
    result = combiner(AFiltred,BFiltred)
    return result

import unittest

class TestUnion(unittest.TestCase):
    def test_bothDifferent(self):
        A = set({"Pol"})
        B = set({"Mathieu"})
        self.assertEqual(union(A,B),set({"Pol","Mathieu"}))

class TestIntersection(unittest.TestCase):
    def test_bothSameAndDifferent(self):
        A = set({"Pol","Baptiste"})
        B = set({"Mathieu","Baptiste"})
        self.assertEqual(intersection(A,B),set({"Baptiste"}))

class TestRetire(unittest.TestCase):
    def test_retireOne(self):
        A = set({"Pol","Baptiste","Mathieu"})
        self.assertEqual(retire("Pol",A),set({"Baptiste","Mathieu"}))

class TestDiff(unittest.TestCase):
    def test_(self):
        A = set({"Pol","Mathieu"})
        B = set({"Mathieu","Baptiste"})
        self.assertEqual(diff(A,B),set({"Pol"}))

class DiffSym(unittest.TestCase):
    def test_(self):
        A = set({"Pol","Mathieu"})
        B = set({"Mathieu","Baptiste"})
        self.assertEqual(diff_sym(A,B),set({"Pol","Baptiste"}))

if __name__ == '__main__':
    unittest.main()