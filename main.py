import func
import copy

def evaluer_clause(clause,list_var):
    if len(clause) == 0:
        return False
    trueCount = 0
    falseCount = 0
    noneCount = 0
    for i in clause:
        temp = i
        valid = True
        if i < 0:
            temp = -i
            valid = False
        if list_var[temp-1] == valid:
            return True
        elif list_var[temp-1] != None:
            falseCount = falseCount+1
        else:
            noneCount = noneCount+1
    if noneCount > 0:
        return None
    return False

def evaluer_cnf(formule,list_var):
    if len(formule) == 0:
        return True
    count = 0
    for i in formule:
        if evaluer_clause(i,list_var):
            count = count+1
    if count == len(formule):
        return True
    return False

def determine_valuations(list_var):
    varIndex = []
    result = []
    for i in range(len(list_var)):
        if list_var[i] == None:
            varIndex.append(i)
    for i in range(0,len(list_var)):
        if func.isInArray(varIndex,i):
            temp2 = []
            switch = True
            if len(result) == 0:
                for x in range(2):
                    temp = copy.copy(list_var)
                    temp[i] = switch
                    temp2.append(temp)
                    switch = not switch
            else :
                for x in result:
                    for y in range(2):
                        current = copy.copy(x)
                        current[i] = switch
                        temp2.append(current)
                        switch = not switch
            result = temp2
    if len(result) == 0:
        temp4 = []
        temp4.append(list_var)
        return temp4
    temp3 = []
    for i in result:
        if func.isInArray(i,True):
            temp3.append(i)
    return temp3

def resol_sat_force_brute(formule,list_var):
    variation = determine_valuations(list_var)
    for i in variation:
        print(i)
        if evaluer_cnf(formule,i):
            return True
    return False

def progress(list_var,list_chgmts):
    result = []
    for i in range(len(list_var)):
        if list_var[i] == None:
            result.append([i,True])
    return result

def retour(list_var,list_chgmts):
    for i in range(1,len(list_chgmts)+1):
        if list_chgmts[len(list_chgmts)-i][1] == True:
            list_chgmts[len(list_chgmts)-i][1] = False
            return list_chgmts
    return list_chgmts

#def resol_parcours_arbre(formule_init,list_var,list_chgmts):
    

import unittest

class TestEvaluerClause(unittest.TestCase):
    def test_Simple(self):
        self.assertTrue(evaluer_clause([-1,2],[False,True]))
    def test_None(self):
        self.assertIsNone(evaluer_clause([1,-2],[None,True]))
    def test_Vide(self):
        self.assertFalse(evaluer_clause([],[]))

class TestEvaluerCNF(unittest.TestCase):
    def test_Simple(self):
        self.assertTrue(evaluer_cnf([[1,-2],[3,-2]],[False,False,False]))
    def test_UnFaux(self):
        self.assertFalse(evaluer_cnf([[1,3],[2,-1]],[True,False,True]))
    def test_FormuleVide(self):
        self.assertTrue(evaluer_cnf([],[]))

class TestEvaluerValuation(unittest.TestCase):
    def test_Simple(self):
        self.assertEquals(determine_valuations([None,None]),[[True,True],[True,False],[False,True]])
    def test_complique(self):
        self.assertEquals(determine_valuations([None,None,None]),[[True,True,True],[True,True,False],[True,False,True],[True,False,False],[False,True,True],[False,True,False],[False,False,True]])
    def test_Contrainte(self):
        self.assertEquals(determine_valuations([True,None]),[[True,True],[True,False]])
    def test_Piege(self):
        self.assertEquals(determine_valuations([True,True]),[[True,True]])

class TestResolvabilité(unittest.TestCase):
    def test_Simple(self):
        self.assertTrue(resol_sat_force_brute([[1,2]],[None,None]))
    def test_Simple2(self):
        self.assertFalse(resol_sat_force_brute([[1,-2]],[False,True]))
    def test_Complique(self):
        self.assertFalse(resol_sat_force_brute([[-1,2],[3,1]],[True,False,False]))
    def test_Complique2(self):
        self.assertFalse(resol_sat_force_brute([[1,2],[1,3]],[False,None,False]))

class TestProgress(unittest.TestCase):
    def test_Enonce(self):
        self.assertEquals(progress([None,True,None],[]),[[0,True],[2,True]])

class TestRetour(unittest.TestCase):
    def test_Simple(self):
        print(retour([None,True,None],progress([None,True,None],[])),)
        self.assertEquals(retour([None,True,None],progress([None,True,None],[])),[[0,True],[2,False]])

if __name__ == '__main__':
    unittest.main()