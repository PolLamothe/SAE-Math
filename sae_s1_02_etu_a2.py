import func
import copy
import time

#TROIS PETITES FONCTIONS DE TEST UTILISEES PLUS BAS#
def test(mess,eval,res):
    print(mess,(eval==res)*'OK'+(eval!=res)*'Try again')
def test_determine_valuations(mess,list_var,res):
    test=mess+'Ok'
    list_testee=determine_valuations(list_var)
    for el in list_testee :
        if el not in res:
            test=mess+'Try again'
            return test
    for el in res:
        if el not in list_testee :
            test=mess+'Try again'
            return test
    for i in range(len(list_testee)-1):
        if list_testee[i] in list_testee[i+1:]:
            test=mess+'wowowow y a du doublon là-dedans'
            return test
    return test  

def test_for(mess,formu,res_for):
    res=True
    if (formu==[] and res_for!=[]) or (formu!=[] and res_for==[]):
        res=False
    for el1 in formu:
        for el2 in res_for:
            res=(set(el1)==set(el2))
            if res :
                break
        if not res :
            print(mess+'Try again !')
            return
    for el2 in res_for:
        for el1 in formu:
            res=(set(el2)==set(el1))
            if res :
                break
        if not res :
            print(mess+'Try again !')
            return
    res=False
    for i in range(len(formu)-1):
        for el in formu[i+1:]:
            if set(formu[i])==set(el):
                print(mess+'wowowow y a du doublon là-dedans')
                return 
    print(mess+'Ok')
    
#A VOUS DE JOUER#
def evaluer_clause(clause,list_var):
    if len(clause) == 0:
        return False
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
    
clause1=[1,-2,3,-4]
list_var1=[True,True,False,None]
test("essai cas 1 evaluer_clause : ",evaluer_clause(clause1,list_var1),True)
clause2=[1,-2,3,-4]
list_var2=[False,True,False,None]
test("essai cas 2 evaluer_clause : ",evaluer_clause(clause2,list_var2),None)
clause3=[1,-2,3,-4]
list_var3=[None,True,False,True]
test("essai cas 3 evaluer_clause : ",evaluer_clause(clause3,list_var3),None)
clause4=[1,-3]
list_var4=[False,False,True]
test("essai cas 4 evaluer_clause : ",evaluer_clause(clause4,list_var4),False)
clause5=[]
list_var5=[False,False,True]
test("essai cas 5 evaluer_clause : ",evaluer_clause(clause5,list_var5),False)
clause6=[1,2,3]
list_var6=[False,False,True]
test("essai cas 6 evaluer_clause : ",evaluer_clause(clause6,list_var6),True)


def evaluer_cnf(formule,list_var):
    if len(formule) == 0:
        return True
    count = 0
    noneCount = 0
    for i in formule:
        if evaluer_clause(i,list_var) == True:
            count = count+1
        elif evaluer_clause(i,list_var) == None:
            noneCount = noneCount+1
    if count == len(formule):
        return True
    if noneCount > 0:
        return None
    return False
    
for1=[[1,2],[2,-3,4],[-1,-2],[-1,-2,-3],[1]]
list_var_for1_test1=[True,False,False,None]
test('test1 evaluer_cnf : ',evaluer_cnf(for1,list_var_for1_test1),True)
list_var_for1_test2=[None,False,False,None]
test('test2 evaluer_cnf : ',evaluer_cnf(for1,list_var_for1_test2),None)
list_var_for1_test3=[True,False,True,False]
test('test3 evaluer_cnf : ',evaluer_cnf(for1,list_var_for1_test3),False)

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
        temp3.append(i)
    return temp3
    

list_var1=[True,None,False,None]
print(test_determine_valuations('res_test_determine_valuations cas 1 : ',list_var1,[[True, True, False, True], [True, False, False, True], [True, True, False, False], [True, False, False, False]]))
list_var2=[None,False,True,None,True,False]
print(test_determine_valuations('res_test_determine_valuations cas 2 : ',list_var2,[[True, False, True, True, True, False], [False, False, True, True, True, False], [True, False, True, False, True, False], [False, False, True, False, True, False]]))
list_var3=[False,True,True,False]
print(test_determine_valuations('res_test_determine_valuations cas 3 : ',list_var3,[[False, True, True, False]]))
list_var4=[None,None,None]
print(test_determine_valuations('res_test_determine_valuations cas 4 : ',list_var4,[[True, True, True], [False, True, True], [True, False, True], [False, False, True], [True, True, False], [False, True, False], [True, False, False], [False, False, False]]))


def resol_sat_force_brute(formule,list_var):
    variation = determine_valuations(list_var)
    for i in variation:
        if evaluer_cnf(formule,i):
            return True,i
    return False,[]

for1=[[1,2],[2,-3,4],[-1,-2],[-1,-2,-3],[1],[-1,2,3]]
list_var_for1=[None,None,None,None]
test('test1 resol_sat_force_brute : ',resol_sat_force_brute(for1,list_var_for1),(True,[True, False, True, True]))

for2=[[1,4,-5],[-1,-5],[2,-3,5],[2,-4],[2,4,5],[-1,-2],[-1,2,-3],[-2,4,-5],[1,-2]]
list_var_for2=[None,None,None,None,None]
test('test2 resol_sat_force_brute : ',resol_sat_force_brute(for2,list_var_for2),(False,[]))

for3=[[-1,-2],[-1,2,-3,4],[2,3,4],[3],[1,-4],[-1,2],[1,2]]
list_var_for3=[None,None,None,None]
test('test3 resol_sat_force_brute : ',resol_sat_force_brute(for3,list_var_for3),(True,[False, True, True, False]))

for4=[[-1,-2],[-1,2,-3,4],[2,3,4],[3],[1,-4],[-1,2],[1,2]]
list_var_for4=[None,None,None,True]
test('test4 resol_sat_force_brute : ',resol_sat_force_brute(for4,list_var_for4),(False,[]))


def enlever_litt_for(formule,litteral):
    result = []
    for i in formule:
        copy = i
        state = True
        for x in i:
            if x == litteral:
                state = False
            if x == litteral*-1:
                copy = func.removeFromArray(copy,x)
        if state:
            result.append(copy)
    return result
    
for1=[[1,2,4,-5],[-1,2,3,-4],[-1,-2,-5],[-3,4,5],[-2,3,4,5],[-4]]
litt1=4
test('essai cas 1 enlever_litt_for : ',enlever_litt_for(for1,litt1),[[-1, 2, 3], [-1, -2, -5], []])

def init_formule_simpl_for(formule_init,list_var):
    import copy
    result = []
    for i in formule_init:
        copy = i
        runned = False
        for x in i:
            if x > 0:
                absolute = x
            else:
                absolute = -x
            if list_var[absolute-1] != None:
                if list_var[absolute-1] == (x > 0):
                    copy = []
                    runned = True
                elif runned == False:
                    copy = func.removeFromArray(copy,x)
        if copy != []:
            result.append(copy)
    return result

list_var_for1=[False, None, None, False, None]
for1=[[-5, -3, 4, -1], [3], [5, -2], [-2, 1, -4], [1, -3]]
cor_for1=[[3], [5, -2], [-3]]
test_for('test1_init_formule_simpl_for : ',init_formule_simpl_for(for1,list_var_for1),cor_for1)

list_var_for2= [False, True, False, True, False]
for2= [[3, 2, 1], [-1, -2, 5]]
cor_for2=[]
test_for('test2_init_formule_simpl_for : ',init_formule_simpl_for(for2,list_var_for2),cor_for2)

list_var_for3= [None, None, None, True, None]
for3= [[-5, -1], [-1, -3], [4], [-4, 1], [-2, -1, 3]]
cor_for3=[[-5, -1], [-1, -3], [1], [-2, -1, 3]]
test_for('test3_init_formule_simpl_for : ',init_formule_simpl_for(for3,list_var_for3),cor_for3)


def retablir_for(formule_init,list_chgmts):
    result = []
    for i in formule_init:
        processed = False
        temp = copy.copy(i)
        for x in i:
            absolute = x
            if x <0:
                absolute = -x
            for y in list_chgmts:
                if y[0]+1 == absolute:
                    if ((x> 0)!= (y[1])) and not processed:
                        temp = func.removeFromArray(temp,x)
                    else:
                        processed = True
        if not processed:
            result.append(temp)
    return result


formule_init=[[1, 2, 4, -5], [-1, 2, 3, -4], [-1, -2, -5], [-3, 4, 5], [-2, 3, 4, 5], [-4, 5]]
list_chgmts1=[[0, True], [1, True], [2, False]]
form1=[[-5], [4, 5], [-4, 5]]

list_chgmts2=[[0, True], [1, True], [2, False], [3, True], [4, False]]
form2=[[]]

list_chgmts3=[[0, True], [1, True], [2, False], [3, False]]
form3=[[-5], [5]]
test('essai cas 1 retablir_for : ',retablir_for(formule_init,list_chgmts1),form1)
test('essai cas 2 retablir_for : ',retablir_for(formule_init,list_chgmts2),form2)
test('essai cas 3 retablir_for : ',retablir_for(formule_init,list_chgmts3),form3)

def progress(list_var,list_chgmts):
    switch = False
    rejectedList = []
    list_var_copy = copy.copy(list_var)
    counter = 0
    for i in range(len(list_var)):
        if list_var[i] != None:
            for x in list_chgmts:
                if x[0] == i:
                    switch = True
            if switch:
                constant = True
                for x in list_chgmts:
                    if x[0] == i:
                        constant = False
                if constant:
                    list_var_copy.pop(i-counter)
                    counter = counter +1
                    rejectedList.append([list_var[i],i])
    list_var = list_var_copy
    for i in range(len(list_var)-2,-1,-1):
        if list_var[i] != None and list_var[i+1] == None:
            list_var[i+1] = True
            list_chgmts.append([i+1,True])
    if list_var[0] == None:
        list_var[0] = True
        list_chgmts.append([0,True])
    for i in rejectedList:
        if i[1] >= len(list_var):
            list_var.append(i[0])
        else:
            list_var = func.decalRight(list_var,i[1],i[0])
        for x in list_chgmts:
            if x[0] >= i[1]:
                x[0] = x[0]+1
    return list_var,list_chgmts

list_var=[True, None, None, None, None]
list_chgmts=[[0, True]]
l1=[True, True, None, None, None]
l2=[[0, True], [1, True]]
test("essai cas 1 progress : ",progress(list_var,list_chgmts),(l1,l2))

list_var=[True, False, False, None, None]
list_chgmts=[[0, True], [1, False], [2, False]]
l1=[True, False, False, True, None]
l2=[[0, True], [1, False], [2, False], [3, True]]
test("essai cas 2 progress : ",progress(list_var,list_chgmts),(l1,l2))

list_var=[None, None, None, None, None]
list_chgmts=[]
l1=[True, None, None, None, None]
l2=[[0, True]]
test("essai cas 3 progress : ",progress(list_var,list_chgmts),(l1,l2))

list_var=[False, None, None, None, None]
list_chgmts=[[0, False]]
l1=[False, True, None, None, None]
l2=[[0, False], [1, True]]
test("essai cas 4 progress : ",progress(list_var,list_chgmts),(l1,l2))

list_var=[True, False, None, None, None]
list_chgmts=[]
l1=[True, False, True, None, None]
l2=[[2, True]]
test("essai cas 5 progress : ",progress(list_var,list_chgmts),(l1,l2))

list_var=[True, False, False, None, None]
list_chgmts=[[2, False]]
l1=[True, False, False, True, None]
l2=[[2, False], [3, True]]
test("essai cas 6 progress : ",progress(list_var,list_chgmts),(l1,l2))

test("essai cas 7 progress (perso)",progress([True, False, None, False, True],[[0, True]]),([True, False, True,False,True],[[0,True],[2, True]]))

def progress_simpl_for(formule,list_var,list_chgmts):
    list_var,list_chgmts = progress(list_var,list_chgmts)
    if init_formule_simpl_for(formule,list_var) == []:
        return [[]],list_var,list_chgmts  
    return init_formule_simpl_for(formule,list_var),list_var,list_chgmts    

formule= [[1, 2, 4, -5], [-1, 2, 3, -4], [-1, -2, -5], [-3, 4, 5], [-2, 3, 4, 5], [-4, 5]] 
list_var= [None, None, None, None, None] 
list_chgmts= []
cor_form,cor_l1,cor_l2= ([[2, 3, -4], [-2, -5], [-3, 4, 5], [-2, 3, 4, 5], [-4, 5]],[True, None, None, None, None],[[0, True]])
test('essai1_progress_simpl_for : ',progress_simpl_for(formule,list_var,list_chgmts),(cor_form,cor_l1,cor_l2))
 
 
formule= [[-5], [5]] 
list_var= [True, True, True, False, None] 
list_chgmts= [[0, True], [1, True], [2, True], [3, False]]
cor_form,cor_l1,cor_l2= ([[]],[True, True, True, False, True],[[0, True], [1, True], [2, True], [3, False], [4, True]])
test('essai2_progress_simpl_for : ',progress_simpl_for(formule,list_var,list_chgmts),(cor_form,cor_l1,cor_l2))

formule= [[3, -4], [-3, 4, 5], [-4, 5]] 
list_var= [True, False, None, None, None] 
list_chgmts= [[0, True], [1, False]]
cor_form,cor_l1,cor_l2= ([[4, 5], [-4, 5]],[True, False, True, None, None],[[0, True], [1, False], [2, True]])
test('essai3_progress_simpl_for : ',progress_simpl_for(formule,list_var,list_chgmts),(cor_form,cor_l1,cor_l2))

def progress_simpl_for_dpll(formule,list_var,list_chgmts,list_sans_retour):
    maping = {"pos":0,"neg":0,"value":0}
    processed = False
    for i in range(len(list_var)):
        if list_var[i] == None:
            pos = 0
            neg = 0
            for x in formule:
                if func.isInArray(x,i+1):
                    pos = pos + 1
                if func.isInArray(x,-(i+1)):
                    neg = neg + 1
                if len(x) == 1 and (func.isInArray(x,i+1)or func.isInArray(x,-(i+1))) and not processed:
                    if func.isInArray(x,i+1):
                        maping = {"pos":1,"neg":0,"value":i+1}
                    else:
                        maping = {"pos":0,"neg":1,"value":i+1}
                    processed = True
            if (pos == 0 or neg == 0) and (pos != 0 or neg != 0) and not processed:
                if pos == 0:
                    maping = {"pos":0,"neg":1,"value":i+1}
                else:
                    maping = {"pos":1,"neg":0,"value":i+1}
                processed = True
    if not processed:
        if formule[0][0] > 0:
            maping = {"pos":1,"neg":0,"value":formule[0][0]}
        else:
            maping = {"pos":0,"neg":1,"value":-(formule[0][0])}
    if maping["pos"] > maping["neg"]:
        if processed:
            list_sans_retour.append(maping["value"]-1)
        list_chgmts.append([maping["value"]-1,True])
        list_var[maping["value"]-1] = True
        formule = init_formule_simpl_for(formule,list_var)
        return formule,list_var,list_chgmts,list_sans_retour
    else:
        list_sans_retour.append(maping["value"]-1)
        list_chgmts.append([maping["value"]-1,False])
        list_var[maping["value"]-1] = False
        formule = init_formule_simpl_for(formule,list_var)
        return formule,list_var,list_chgmts,list_sans_retour

formule= [[-5], [4, 5], [-4, 5]] 
list_var= [True, True, False, None, None] 
list_chgmts= [[0, True], [1, True], [2, False]] 
list_sans_retour= []
cor_for,cor_l1,cor_l2,cor_l3= ([[4], [-4]],[True, True, False, None, False],[[0, True], [1, True], [2, False], [4, False]],[4])
test('essai1_progress_simpl_for_dpll : ',progress_simpl_for_dpll(formule,list_var,list_chgmts,list_sans_retour),(cor_for,cor_l1,cor_l2,cor_l3))

formule= [[-5,4], [2,4, 5], [-2, 5]]
list_var= [True, None, None, None, None]
list_chgmts= [[0, True]] 
list_sans_retour= [0]
cor_for,cor_l1,cor_l2,cor_l3= ([[-2,5]],[True, None, None, True, None],[[0, True],[3, True]],[0,3])
test('essai2_progress_simpl_for_dpll : ',progress_simpl_for_dpll(formule,list_var,list_chgmts,list_sans_retour),(cor_for,cor_l1,cor_l2,cor_l3))

formule=[[1,2,4,-5],[-1,2,3,-4],[-1,-2,-5],[-3,4,5],[-2,3,4,5],[-4,5]]
list_var=[None,None,None,None,None]
list_chgmts= [] 
list_sans_retour= []
cor_for,cor_l1,cor_l2,cor_l3=([[2, 3, -4], [-2, -5], [-3, 4, 5], [-2, 3, 4, 5], [-4, 5]], [True, None, None, None, None], [[0, True]], [])
test('essai3_progress_simpl_for_dpll : ',progress_simpl_for_dpll(formule,list_var,list_chgmts,list_sans_retour),(cor_for,cor_l1,cor_l2,cor_l3))


def retour(list_var,list_chgmts):#True -> False/False -> None
    for i in range(len(list_var)-1,-1,-1):
        valid = False
        for x in list_chgmts:
            if x[0] == i:
                valid = True
        if valid:
            if list_var[i] == True:
                for x in range(len(list_chgmts)):
                    if list_chgmts[x][0] == i:
                        list_chgmts[x][1] = False
                list_var[i] = False 
                return list_var,list_chgmts
            else:
                list_var[i] = None
                list_chgmts.pop()
    return list_var,list_chgmts

list_var= [True, True, None, None, None]
list_chgmts= [[0, True], [1, True]]
l1= [True, False, None, None, None]
l2= [[0, True], [1, False]]
test("essai cas 1 retour : ",retour(list_var,list_chgmts),(l1,l2))

list_var= [True, False, None, None, None]
list_chgmts= [[0, True], [1, False]]
l1= [False, None, None, None, None]
l2= [[0, False]]
test("essai cas 2 retour : ",retour(list_var,list_chgmts),(l1,l2))

list_var= [True, False, False, True, None]
list_chgmts= []
l1= [True, False, False, True, None]
l2= []
test("essai cas 3 retour : ",retour(list_var,list_chgmts),(l1,l2))

list_var= [True, False, False, False, False]
list_chgmts= [[0, True], [1, False], [2, False], [3, False], [4, False]]
l1= [False, None, None, None, None]
l2= [[0, False]]
test("essai cas 4 retour : ",retour(list_var,list_chgmts),(l1,l2))

list_var= [True, True, False, True, None]
list_chgmts= [[1, True]]
l1= [True, False, False, True, None]
l2= [[1, False]]
test("essai cas 5 retour : ",retour(list_var,list_chgmts),(l1,l2))

list_var= [True, False, False, True, None]
list_chgmts= [[1, False]]
l1= [True, None, False, True, None]
l2= []
test("essai cas 6 retour : ",retour(list_var,list_chgmts),(l1,l2))


def retour_simpl_for(formule_init,list_var,list_chgmts):
    list_var,list_chgmts = retour(list_var,list_chgmts)
    formule = retablir_for(formule_init,list_chgmts)
    return formule,list_var,list_chgmts

formule_init= [[-2, 1, -5, -4], [2, 4, -1], [-5, 4], [1, 4, -2], [-4, -2, 5]] 
list_var= [True, True, False, False, True] 
list_chgmts= [[0, True], [4, True]]
cor_form,cor_l1,cor_l2= ([[2, 4], [-4, -2]],[True, True, False, False, False],[[0, True], [4, False]])
test('essai1_retour_simpl_for : ',retour_simpl_for(formule_init,list_var,list_chgmts),(cor_form,cor_l1,cor_l2))

formule_init= [[5, 4, -3], [-2, -5, 3], [-1]] 
list_var= [False, True, True, False, False] 
list_chgmts= [[2, True]]
cor_form,cor_l1,cor_l2= ([[-2, -5], [-1]],[False, True, False, False, False],[[2, False]])
test('essai2_retour_simpl_for : ',retour_simpl_for(formule_init,list_var,list_chgmts),(cor_form,cor_l1,cor_l2))

formule_init= [[1, 2, 4, -5], [-1, 2, 3, -4], [-1, -2, -5], [-3, 4, 5], [-2, 3, 4, 5], [-4, 5]] 
list_var= [True, True, None, None, False] 
list_chgmts= [[0, True], [1, True], [4, False]] 
cor_form,cor_l1,cor_l2= ([[3, -4], [-3, 4, 5], [-4, 5]], [True, False, None, None, None], [[0, True], [1, False]])
test('essai2_retour_simpl_for : ',retour_simpl_for(formule_init,list_var,list_chgmts),(cor_form,cor_l1,cor_l2))

def retour_simpl_for_dpll(formule_init,list_var,list_chgmts,list_sans_retour):
    for i in list_sans_retour:
        list_var[i] = None
        for x in range(len(list_chgmts)-1):
            if list_chgmts[x][0] == i:
                del list_chgmts[x]
    formule_init,list_var,list_chgmts = retour_simpl_for(formule_init,list_var,list_chgmts)
    return (formule_init,list_var,list_chgmts,[])

formule_init= [[1, 2, 4, -5], [-1, 2, 3, -4], [-1, -2, -5], [-3, 4, 5], [-2, 3, 4, 5], [-4, 5]] 
list_var= [True, True, False, True, False] 
list_chgmts= [[0, True], [1, True], [2, False], [4, False], [3, True]] 
list_sans_retour= [4, 3]
cor_form,cor_l1,cor_l2,cor_l3= ([[3, -4], [-3, 4, 5], [-4, 5]], [True, False, None, None, None], [[0, True], [1, False]], [])
test('essai1_retour_simpl_for_dpll : ',retour_simpl_for_dpll(formule_init,list_var,list_chgmts,list_sans_retour),(cor_form,cor_l1,cor_l2,cor_l3))

formule_init= [[1, 2, 4, -5], [-1, 2, 3, -4], [-1, -2, -5], [-3, 4, 5], [-2, 3, 4, 5], [-4, 5]] 
list_var= [True, True, True, True, False] 
list_chgmts= [[0, True], [1, True], [2, True], [3, True], [4, False]] 
list_sans_retour= []
cor_form,cor_l1,cor_l2,cor_l3= ([[-5], [5]], [True, True, True, False, None], [[0, True], [1, True], [2, True], [3, False]], [])
test('essai2_retour_simpl_for_dpll : ',retour_simpl_for_dpll(formule_init,list_var,list_chgmts,list_sans_retour),(cor_form,cor_l1,cor_l2,cor_l3))

formule_init= [[3, 1], [1], [-2, 3, -5], [-1, 3], [-4, -3, -2]] 
list_var= [True, None, False, None, True] 
list_chgmts= [[0, True]] 
list_sans_retour= [0]
cor_form,cor_l1,cor_l2,cor_l3= ([[3, 1], [1], [-2, 3, -5], [-1, 3], [-4, -3, -2]], [None, None, False, None, True], [], [])
test('essai3_retour_simpl_for_dpll : ',retour_simpl_for_dpll(formule_init,list_var,list_chgmts,list_sans_retour),(cor_form,cor_l1,cor_l2,cor_l3))

formule_init= [[3, 1], [1], [-2, 3, -5], [-1, 3], [-4, -3, -2]] 
list_var= [None, None, False, None, True] 
list_chgmts= [] 
list_sans_retour= []
cor_form,cor_l1,cor_l2,cor_l3= ([[3, 1], [1], [-2, 3, -5], [-1, 3], [-4, -3, -2]], [None, None, False, None, True], [], [])
test('essai3_retour_simpl_for_dpll : ',retour_simpl_for_dpll(formule_init,list_var,list_chgmts,list_sans_retour),(cor_form,cor_l1,cor_l2,cor_l3))

def resol_parcours_arbre(formule_init,list_var,list_chgmts):
    if not func.isInArray(list_var,None) and evaluer_cnf(formule_init,list_var):
        if evaluer_cnf(formule_init,list_var):
            return True,list_var
        return False,[]
    elif not func.isInArray(list_var,None) and list_chgmts[len(list_chgmts)-1][1] == False:
        return False,[]
    else:
        if evaluer_cnf(formule_init,list_var) != False:
            list_var,list_chgmts = progress(list_var,list_chgmts)
        else:
            list_var,list_chgmts = retour(list_var,list_chgmts)
        if list_chgmts == []:
            return False,[]
        return resol_parcours_arbre(formule_init,list_var,list_chgmts)


formule_init= [[1, 4, -5], [-1, -5], [2, -3, 5], [2, -4], [2, 4, 5], [-1, -2], [-1, 2, -3], [-2, 4, -5], [1, -2]] 
list_var= [True, True, False, True, None] 
list_chgmts= [[1, True]]
cor_resol=(False, [])
test('essai1_resol_parcours_arbre : ',resol_parcours_arbre(formule_init,list_var,list_chgmts),cor_resol)

formule_init= [[5], [3, -5, -1, -2], [1, -2, -5], [2, -5, 1, -3], [3]] 
list_var= [True, False, None, False, True] 
list_chgmts= [[0, True]]
cor_resol=(True,[True, False, True, False, True])
test('essai2_resol_parcours_arbre : ',resol_parcours_arbre(formule_init,list_var,list_chgmts),cor_resol)

formule_init= [[-5, 2, -3, -4], [1, -5], [5, 2], [3, -2, 4], [5, -2, -1]] 
list_var= [False, True, False, None, None] 
list_chgmts= [[1, True]]
cor_resol=(True,[False, True, False, True, False])
test('essai3_resol_parcours_arbre : ',resol_parcours_arbre(formule_init,list_var,list_chgmts),cor_resol)

def resol_parcours_arbre_simpl_for(formule_init,formule,list_var,list_chgmts):
    if list_chgmts==[]:
        if [] in formule:
            return False,[]
        if formule==[]:
            return True,list_var
        form,list_var_init,list_chgmts_init=progress_simpl_for(formule.copy(),list_var.copy(),[])
        return resol_parcours_arbre_simpl_for(formule_init,form,list_var_init,list_chgmts_init)
    formuleCounter = 0
    for i in formule:
        if len(i) == 0:
            formuleCounter = formuleCounter +1
    if formuleCounter == len(formule):
        return True,list_var
    advanced1,advanced2,advanced3= progress_simpl_for(formule.copy(),list_var.copy(),list_chgmts.copy())
    if evaluer_cnf(formule_init,advanced2) != False:
        return resol_parcours_arbre_simpl_for(formule_init,advanced1,advanced2,advanced3)
    return1,return2,return3 = retour_simpl_for(formule_init.copy(),advanced2.copy(),advanced3.copy())
    if evaluer_cnf(formule_init,return2) != False:
        return resol_parcours_arbre_simpl_for(formule_init,return1,return2,return3)
    if list_chgmts[len(list_chgmts)-1][1] != False:
        return1,return2,return3 = retour_simpl_for(formule_init.copy(),list_var,list_chgmts.copy())
        return resol_parcours_arbre_simpl_for(formule_init.copy(),return1,return2,return3)
    else:
        for i in list_chgmts:
            if i[1] != False:
                return1,return2,return3 = retour_simpl_for(formule_init.copy(),list_var.copy(),list_chgmts.copy())
                return resol_parcours_arbre_simpl_for(formule_init,return1,return2,return3)
        return False,[]

formule_init= [[1, 2, 4, -5], [-1, 2, 3, -4], [-1, -2, -5], [-3, 4, 5], [-2, 3, 4, 5], [-4, 5]] 
formule= [[2, 3, -4], [-2, -5], [-3, 4, 5], [-2, 3, 4, 5], [-4, 5]] 
list_var= [True, None, None, None, None] 
list_chgmts= [[0, True]]
cor_resol=(True, [True, False, True, True, True])
test('essai1_resol_parcours_arbre_simpl_for : ',resol_parcours_arbre_simpl_for(formule_init,formule,list_var,list_chgmts),cor_resol)

formule_init= [[5], [3, -5, -1, -2], [1, -2, -5], [2, -5, 1, -3], [3]] 
formule= [[5], [-5]] 
list_var= [False, True, True, False, None] 
list_chgmts= [[2, True]]
cor_resol=(False, [])
test('essai2_resol_parcours_arbre_simpl_for : ',resol_parcours_arbre_simpl_for(formule_init,formule,list_var,list_chgmts),cor_resol)

formule_init= [[-5, 2, -3, -4], [1, -5], [5, 2], [3, -2, 4], [5, -2, -1]] 
formule= [[-5], [4]] 
list_var= [False, True, False, None, None] 
list_chgmts= [[1, True]]
cor_resol=(True, [False, True, False, True, False])
test('essai3_resol_parcours_arbre_simpl_for : ',resol_parcours_arbre_simpl_for(formule_init,formule,list_var,list_chgmts),cor_resol)

formule_init= [[-5, 2, -3, -4], [1, -5], [5, 2], [3, -2, 4], [5, -2, -1]] 
list_var= [False, True, False, None, None] 
list_chgmts= [[1, True]]
cor_resol=(True,[False, True, False, True, False])
test('essai4_resol_parcours_arbre_simpl_for : ',resol_parcours_arbre_simpl_for(formule_init,formule_init,list_var,list_chgmts),cor_resol)

formule_init= [[1, 4, -5], [-1, -5], [2, -3, 5], [2, -4], [2, 4, 5], [-1, -2], [-1, 2, -3], [-2, 4, -5], [1, -2]] 
list_var= [True, True, False, True, None] 
list_chgmts= [[1, True]]
cor_resol=(False, [])
test('essai5_resol_parcours_arbre_simpl_for : ',resol_parcours_arbre_simpl_for(formule_init,formule_init,list_var,list_chgmts),cor_resol)

def resol_parcours_arbre_simpl_for_dpll(formule_init,formule,list_var,list_chgmts,list_sans_retour):
    #Initialisation du parcours
    if list_chgmts==[]:
        if [] in formule:
            return False,[]
        form,list_var_init,list_chgmts_init,list_sans_retour_init=progress_simpl_for_dpll(formule,list_var,[],[])
        return resol_parcours_arbre_simpl_for_dpll(formule_init,form,list_var_init,list_chgmts_init,list_sans_retour_init)
    if formule == []:
        return True,list_var
    advanced1,advanced2,advanced3,advanced4 = progress_simpl_for_dpll(formule.copy(),list_var.copy(),list_chgmts.copy(),list_sans_retour.copy())
    if evaluer_cnf(formule_init,advanced2) != False:
        return resol_parcours_arbre_simpl_for_dpll(formule_init,advanced1,advanced2,advanced3,advanced4)
    return1,return2,return3,return4 = retour_simpl_for_dpll(formule_init,advanced2,advanced3,advanced4)
    if evaluer_cnf(formule_init,return2) != False:
        if return3 == []:
            return False,[]
        return resol_parcours_arbre_simpl_for_dpll(formule_init,return1,return2,return3,return4)
    else:
        for i in list_chgmts:
            if i[1] != False:
                    return1,return2,return3,return4 = retour_simpl_for_dpll(formule_init,list_var,list_chgmts,list_sans_retour)
                    return resol_parcours_arbre_simpl_for_dpll(formule_init,return1,return2,return3,return4)
        return False,[]

formule_init= [[1, 2, 4, -5], [-1, 2, 3, -4], [-1, -2, -5], [-3, 4, 5], [-2, 3, 4, 5], [-4, 5]] 
formule= [[2, 3, -4], [-2, -5], [-3, 4, 5], [-2, 3, 4, 5], [-4, 5]] 
list_var= [True, None, None, None, None] 
list_chgmts= [[0, True]] 
list_sans_retour= []
cor_resol=(True, [True, False, True, None, True])
test('essai1_resol_parcours_arbre_simpl_for_dpll : ',resol_parcours_arbre_simpl_for_dpll(formule_init,formule,list_var,list_chgmts,list_sans_retour),cor_resol)

formule_init= [[1, 2, 4, -5], [-1, 2, 3, -4], [-1, -2, -5], [-3, 4, 5], [-2, 3, 4, 5], [-4, 5]] 
formule= [[3, -4]] 
list_var= [True, False, None, None, True] 
list_chgmts= [[0, True], [1, False], [4, True]] 
list_sans_retour= [4]
cor_resol=(True, [True, False, True, None, True])
test('essai2_resol_parcours_arbre_simpl_for_dpll : ',resol_parcours_arbre_simpl_for_dpll(formule_init,formule,list_var,list_chgmts,list_sans_retour),cor_resol)

formule_init= [[-5, 2, -3, -4], [1, -5], [5, 2], [3, -2, 4], [5, -2, -1]] 
formule= [[2], [-2, 4]] 
list_var= [False, None, False, None, False] 
list_chgmts= [[4, False]] 
list_sans_retour= [4]
cor_resol=(True, [False, True, False, True, False])
test('essai3_resol_parcours_arbre_simpl_for_dpll : ',resol_parcours_arbre_simpl_for_dpll(formule_init,formule,list_var,list_chgmts,list_sans_retour),cor_resol)

formule_init= [[5], [3, -5, -1, -2], [1, -2, -5], [2, -5, 1, -3], [3]] 
formule= [[-2],[2,-3],[3]] 
list_var= [False, None, None, False, True] 
list_chgmts= [[4, True]]
list_sans_retour=[4]
cor_resol=(False, [])
test('essai4_resol_parcours_arbre_simpl_for_dpll : ',resol_parcours_arbre_simpl_for_dpll(formule_init,formule,list_var,list_chgmts,list_sans_retour),cor_resol)

formule_init= [[1, 4, -5], [-1, -5], [2, -3, 5], [2, -4], [2, 4, 5], [-1, -2], [-1, 2, -3], [-2, 4, -5], [1, -2]] 
list_var= [True, True, False, True, None] 
list_chgmts= [[1, True]]
cor_resol=(False, [])
test('essai1_resol_parcours_arbre : ',resol_parcours_arbre_simpl_for_dpll(formule_init,init_formule_simpl_for(formule_init,list_var),list_var,list_chgmts,[1]),cor_resol)

def ultim_resol(formule_init,list_var):
    '''
    Renvoie SAT,l1 avec :
SAT=True ou False
l1=une liste de valuations rendant la formule vraie ou une liste vide

    Affichage possible du temps mis pour la résolution
'''

def ultim_resol_simpl_for(formule_init,list_var):
    '''
    Renvoie SAT,l1 avec :
SAT=True ou False
l1=une liste de valuations rendant la formule vraie ou une liste vide

    Affichage possible du temps mis pour la résolution
'''

def ultim_resol_simpl_for_dpll(formule_init,list_var):
    '''
    Renvoie SAT,l1 avec :
SAT=True ou False
l1=une liste de valuations rendant la formule vraie ou une liste vide

    Affichage possible du temps mis pour la résolution
'''

def creer_grille_init(list_grille,n):
    '''Arguments : une liste de listes(contenant les coordonnées à renseigner et le nombre correspondant) et un entier donnant la taille de la grille
        Renvoie : une liste (list_grille_complete) avec les valeurs qui devront s'afficher dans la grille en la parcourant ligne après ligne de haut en bas et de gauche à droite
'''
'''
list_grille3=[[1,3,2],[1,6,5],[2,5,4],[2,8,9],[2,9,3],[3,2,7],[3,9,6],[4,3,1],[4,4,8],[4,8,3],[5,1,7],[5,2,2],[5,5,6],[5,8,8],[5,9,4],[6,2,4],[6,6,2],[6,7,5],[7,1,3],[7,8,1],[8,1,4],[8,2,6],[8,5,7],[9,4,9],[9,7,8]]
cor_grille3=[0, 0, 2, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 9, 3, 0, 7, 0, 0, 0, 0, 0, 0, 6, 0, 0, 1, 8, 0, 0, 0, 3, 0, 7, 2, 0, 0, 6, 0, 0, 8, 4, 0, 4, 0, 0, 0, 2, 5, 0, 0, 3, 0, 0, 0, 0, 0, 0, 1, 0, 4, 6, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 8, 0, 0]
test("essai creer_grille_init : ",creer_grille_init(list_grille3,3),cor_grille3)
'''
def creer_grille_final(list_var,n):
    '''
    Renvoie : une liste (list_grille_complete) avec les valeurs qui devront s'afficher dans la grille (en fonction des valeurs logiques prises par les variables de list_var) en la parcourant ligne après ligne de haut en bas et de gauche à droite
'''
'''
list_var_fin=[False, False, False, False, False, False, False, False, True, False, False, True, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, True, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, True, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, True, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, True, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, True, False, True, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, True, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, True, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, True, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, True, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, True, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, True, False, True, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, True, False, False, False, True, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, True, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, True, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, True, False, False, True, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, True, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, True, False, False, True, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, True, False, False, False, False, False, False, False, False, False, True, False, False, False, False]
cor_grille_final=[9, 3, 2, 6, 1, 5, 4, 7, 8, 5, 8, 6, 2, 4, 7, 1, 9, 3, 1, 7, 4, 3, 8, 9, 2, 5, 6, 6, 9, 1, 8, 5, 4, 7, 3, 2, 7, 2, 5, 1, 6, 3, 9, 8, 4, 8, 4, 3, 7, 9, 2, 5, 6, 1, 3, 5, 9, 4, 2, 8, 6, 1, 7, 4, 6, 8, 5, 7, 1, 3, 2, 9, 2, 1, 7, 9, 3, 6, 8, 4, 5]
test("essai creer_grille_final : ",creer_grille_final(list_var_fin,3),cor_grille_final)
'''
def afficher_grille(grille,n):
    '''
    ça affiche la grille
'''

def for_conj_sudoku(n):
    '''
    Renvoie : la formule (liste de listes) associée à une grille de sudoku de taille n selon les attentes formulées dans le sujet
    '''
'''
corrige_for2=[[-1, -21], [-1, -5], [-1, -17], [-1, -9], [-1, -33], [-1, -13], [-1, -49], [-1, -2], [-1, -3], [-1, -4], [-5, -17], [-5, -9], [-17, -33], [-5, -13], [-17, -49], [-5, -6], [-5, -7], [-5, -8], [-9, -13], [-33, -49], [-9, -10], [-9, -11], [-9, -12], [-13, -14], [-13, -15], [-13, -16], [1, 5, 9, 13], [1, 17, 33, 49], [1, 5, 17, 21], [-9, -29], [-17, -21], [-5, -21], [-17, -25], [-5, -37], [-17, -29], [-5, -53], [-17, -18], [-17, -19], [-17, -20], [-13, -25], [-21, -25], [-21, -37], [-21, -29], [-21, -53], [-21, -22], [-21, -23], [-21, -24], [-25, -29], [-37, -53], [-25, -26], [-25, -27], [-25, -28], [-29, -30], [-29, -31], [-29, -32], [17, 21, 25, 29], [5, 21, 37, 53], [9, 13, 25, 29], [-33, -53], [-33, -37], [-9, -25], [-33, -41], [-9, -41], [-33, -45], [-9, -57], [-33, -34], [-33, -35], [-33, -36], [-37, -49], [-37, -41], [-25, -41], [-37, -45], [-25, -57], [-37, -38], [-37, -39], [-37, -40], [-41, -45], [-41, -57], [-41, -42], [-41, -43], [-41, -44], [-45, -46], [-45, -47], [-45, -48], [33, 37, 41, 45], [9, 25, 41, 57], [33, 37, 49, 53], [-41, -61], [-49, -53], [-13, -29], [-49, -57], [-13, -45], [-49, -61], [-13, -61], [-49, -50], [-49, -51], [-49, -52], [-45, -57], [-53, -57], [-29, -45], [-53, -61], [-29, -61], [-53, -54], [-53, -55], [-53, -56], [-57, -61], [-45, -61], [-57, -58], [-57, -59], [-57, -60], [-61, -62], [-61, -63], [-61, -64], [49, 53, 57, 61], [13, 29, 45, 61], [41, 45, 57, 61], [-2, -22], [-2, -6], [-2, -18], [-2, -10], [-2, -34], [-2, -14], [-2, -50], [-2, -3], [-2, -4], [-6, -18], [-6, -10], [-18, -34], [-6, -14], [-18, -50], [-6, -7], [-6, -8], [-10, -14], [-34, -50], [-10, -11], [-10, -12], [-14, -15], [-14, -16], [2, 6, 10, 14], [2, 18, 34, 50], [2, 6, 18, 22], [-10, -30], [-18, -22], [-6, -22], [-18, -26], [-6, -38], [-18, -30], [-6, -54], [-18, -19], [-18, -20], [-14, -26], [-22, -26], [-22, -38], [-22, -30], [-22, -54], [-22, -23], [-22, -24], [-26, -30], [-38, -54], [-26, -27], [-26, -28], [-30, -31], [-30, -32], [18, 22, 26, 30], [6, 22, 38, 54], [10, 14, 26, 30], [-34, -54], [-34, -38], [-10, -26], [-34, -42], [-10, -42], [-34, -46], [-10, -58], [-34, -35], [-34, -36], [-38, -50], [-38, -42], [-26, -42], [-38, -46], [-26, -58], [-38, -39], [-38, -40], [-42, -46], [-42, -58], [-42, -43], [-42, -44], [-46, -47], [-46, -48], [34, 38, 42, 46], [10, 26, 42, 58], [34, 38, 50, 54], [-42, -62], [-50, -54], [-14, -30], [-50, -58], [-14, -46], [-50, -62], [-14, -62], [-50, -51], [-50, -52], [-46, -58], [-54, -58], [-30, -46], [-54, -62], [-30, -62], [-54, -55], [-54, -56], [-58, -62], [-46, -62], [-58, -59], [-58, -60], [-62, -63], [-62, -64], [50, 54, 58, 62], [14, 30, 46, 62], [42, 46, 58, 62], [-3, -23], [-3, -7], [-3, -19], [-3, -11], [-3, -35], [-3, -15], [-3, -51], [-3, -4], [-7, -19], [-7, -11], [-19, -35], [-7, -15], [-19, -51], [-7, -8], [-11, -15], [-35, -51], [-11, -12], [-15, -16], [3, 7, 11, 15], [3, 19, 35, 51], [3, 7, 19, 23], [-11, -31], [-19, -23], [-7, -23], [-19, -27], [-7, -39], [-19, -31], [-7, -55], [-19, -20], [-15, -27], [-23, -27], [-23, -39], [-23, -31], [-23, -55], [-23, -24], [-27, -31], [-39, -55], [-27, -28], [-31, -32], [19, 23, 27, 31], [7, 23, 39, 55], [11, 15, 27, 31], [-35, -55], [-35, -39], [-11, -27], [-35, -43], [-11, -43], [-35, -47], [-11, -59], [-35, -36], [-39, -51], [-39, -43], [-27, -43], [-39, -47], [-27, -59], [-39, -40], [-43, -47], [-43, -59], [-43, -44], [-47, -48], [35, 39, 43, 47], [11, 27, 43, 59], [35, 39, 51, 55], [-43, -63], [-51, -55], [-15, -31], [-51, -59], [-15, -47], [-51, -63], [-15, -63], [-51, -52], [-47, -59], [-55, -59], [-31, -47], [-55, -63], [-31, -63], [-55, -56], [-59, -63], [-47, -63], [-59, -60], [-63, -64], [51, 55, 59, 63], [15, 31, 47, 63], [43, 47, 59, 63], [-4, -24], [-4, -8], [-4, -20], [-4, -12], [-4, -36], [-4, -16], [-4, -52], [-8, -20], [-8, -12], [-20, -36], [-8, -16], [-20, -52], [-12, -16], [-36, -52], [4, 8, 12, 16], [4, 20, 36, 52], [4, 8, 20, 24], [-12, -32], [-20, -24], [-8, -24], [-20, -28], [-8, -40], [-20, -32], [-8, -56], [-16, -28], [-24, -28], [-24, -40], [-24, -32], [-24, -56], [-28, -32], [-40, -56], [20, 24, 28, 32], [8, 24, 40, 56], [12, 16, 28, 32], [-36, -56], [-36, -40], [-12, -28], [-36, -44], [-12, -44], [-36, -48], [-12, -60], [-40, -52], [-40, -44], [-28, -44], [-40, -48], [-28, -60], [-44, -48], [-44, -60], [36, 40, 44, 48], [12, 28, 44, 60], [36, 40, 52, 56], [-44, -64], [-52, -56], [-16, -32], [-52, -60], [-16, -48], [-52, -64], [-16, -64], [-48, -60], [-56, -60], [-32, -48], [-56, -64], [-32, -64], [-60, -64], [-48, -64], [52, 56, 60, 64], [16, 32, 48, 64], [44, 48, 60, 64]]
test_for('test_for_conj_sudoku : ',for_conj_sudoku(2),corrige_for2)
'''



def init_list_var(grille,n):
    '''
    Renvoie : une liste list_var initialisant une valuation tenant compte des valeurs non nulles déjà renseignées dans list_grille_complete
'''
'''
grille2= [0, 1, 0, 0, 4, 2, 0, 0, 0, 0, 2, 0, 0, 3, 0, 0]
cor_list_var_grille2= [None, None, None, None, True, False, False, False, None, None, None, None, None, None, None, None, False, False, False, True, False, True, False, False, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, False, True, False, False, None, None, None, None, None, None, None, None, False, False, True, False, None, None, None, None, None, None, None, None]
test('test_init_list_var : ',init_list_var(grille2,2),cor_list_var_grille2)
'''







'''#test ultim_resol
for2=[[1,4,-5],[-1,-5],[2,-3,5],[2,-4],[2,4,5],[-1,-2],[-1,2,-3],[-2,4,-5],[1,-2]]
list_var_for2=[None,None,None,None,None]
boo_for2,lilifor2=ultim_resol(for2,list_var_for2)
print('boo_for2 : ',boo_for2)
print('lilifor2 : ',lilifor2)'''


'''#test ultim_resol_simpl_for
#Cas grille Taille 2
formul_sudok2=for_conj_sudoku(2)
list_grille2=[[1,2,1],[2,1,4],[2,2,2],[3,3,2],[4,2,3]]
list_grille2_f=[[1,2,4],[2,1,4],[2,2,2],[3,3,2],[4,2,3]]
grille2=creer_grille_init(list_grille2,2)
afficher_grille(grille2,2)
list_var_grille2=init_list_var(grille2,2)
boo_2,lili2=ultim_resol_simpl_for(formul_sudok2,list_var_grille2)
#corrigé lili2=[False, False, True, False, True, False, False, False, False, False, False, True, False, True, False, False, False, False, False, True, False, True, False, False, False, False, True, False, True, False, False, False, True, False, False, False, False, False, False, True, False, True, False, False, False, False, True, False, False, True, False, False, False, False, True, False, True, False, False, False, False, False, False, True]
if boo_2:
    afficher_grille(creer_grille_final(lili2,2),2)
grille2f=creer_grille_init(list_grille2_f,2)
afficher_grille(grille2f,2)
list_var_grille2f=init_list_var(grille2f,2)
boo_2f,lili2f=ultim_resol_simpl_for(formul_sudok2,list_var_grille2f)
if boo_2f:
    afficher_grille(creer_grille_final(lili2f,2),2)'''

'''
#test ultim_resol_simpl_for
#Cas grille Taille 3
formul_sudok=for_conj_sudoku(3)
list_grille3=[[1,3,2],[1,6,5],[2,5,4],[2,8,9],[2,9,3],[3,2,7],[3,9,6],[4,3,1],[4,4,8],[4,8,3],[5,1,7],[5,2,2],[5,5,6],[5,8,8],[5,9,4],[6,2,4],[6,6,2],[6,7,5],[7,1,3],[7,8,1],[8,1,4],[8,2,6],[8,5,7],[9,4,9],[9,7,8]]
grille3=creer_grille_init(list_grille3,3)
afficher_grille(grille3,3)
list_var_grille3=init_list_var(grille3,3)
boo_3,lili3=ultim_resol_simpl_for(formul_sudok,list_var_grille3)
if boo_3:
    afficher_grille(creer_grille_final(lili3,3),3)
'''



'''#test ultim_resol_simpl_for_dpll cas3
formul_sudok=for_conj_sudoku(3)
list_grille3=[[1,3,2],[1,6,5],[2,5,4],[2,8,9],[2,9,3],[3,2,7],[3,9,6],[4,3,1],[4,4,8],[4,8,3],[5,1,7],[5,2,2],[5,5,6],[5,8,8],[5,9,4],[6,2,4],[6,6,2],[6,7,5],[7,1,3],[7,8,1],[8,1,4],[8,2,6],[8,5,7],[9,4,9],[9,7,8]]
grille3=creer_grille_init(list_grille3,3)
afficher_grille(grille3,3)
list_var_grille3=init_list_var(grille3,3)
boo_3,lili3=ultim_resol_simpl_for_dpll(formul_sudok,list_var_grille3)
if boo_3:
    afficher_grille(creer_grille_final(lili3,3),3)'''