import itertools


def dfs_change(pw, count, res, pos):
    if count == 0:
        res.append(pw)
        return
    
    for i in range(pos, len(pw) - 1):
        if len(pw) - i < count:
            break

        if pw[i].isupper():
            dfs_change(pw[:i] + pw[i].lower() + pw[i+1:], count - 1, res, i + 1)
        else:
            dfs_change(pw[:i] + pw[i].upper() + pw[i+1:], count - 1, res, i + 1)

def check_capt(pw1,pw2):
    #pw1,pw2 (string,string): a pair of input password
    #output (boolean): if pw1 and pw2 can be transformed by this category of rule
    #e.g. pw1 = abcdE, pw2= abCde, output =True
    
    # ***********************************************************************
    # ****************************** TODO ***********************************
    # ***********************************************************************

    if len(pw2) != len(pw1):
        return False

    pw2_lower = pw2.lower()

    pw1_lower = pw1.lower()
    

    if pw2_lower == pw1_lower:
        return True

    return False 

def check_capt_transformation(pw1, pw2):
    #pw1,pw2 (string,string): a pair of input password
    #output (string): transformation between pw1 and pw2
    #consider if head char is capt transformed, if tail char is capt transformed, and # of chars that has been capt transformed in total
    #example pw1 = abcde, pw2 = AbcDe, transformation = head\t2 (head char is capt transformed, in total 2 chars are capt transformed)
    #example pw1 = abcdE, pw2 = AbcDe, transformation = head\ttail\t3 (head char and tail chars are capt transformed, in total 3 chars are capt transformed)
    #example pw1 = abcde, pw2 = abcDe, transformation = 1 (in total 1 chars are capt transformed)

    # ***********************************************************************
    # ****************************** TODO ***********************************
    # ***********************************************************************

    outputStr = ''

    if pw1[-1] != pw2[-1]:
        outputStr += 'tail\t'
    

    if pw1[0] != pw2[0]:
        outputStr += 'head\t'
    
    
    count = 0
    for i in range(len(pw1)):
        if pw1[i] != pw2[i]:
            count += 1
    outputStr += str(count)

    return outputStr

def apply_capt_transformation(ori_pw, transformation):
    #ori_pw (string): input password that needs to be transformed
    #transformation (string): transformation in string
    #output (list of string): list of passwords that after transformation (all possiblities)
    #ori_pw = "abcde", transformation = "head\t2", output = [ABcde, AbCde, AbcDe]
    
    # ***********************************************************************
    # ****************************** TODO ***********************************
    # ***********************************************************************

    trans_pw = []

    possible_pw = ''
    count = int(transformation.split('\t')[-1])

    if transformation.find('head') != -1:
        count -= 1
        if ori_pw[0].isupper():
            possible_pw = ori_pw[0].lower() + ori_pw[1:]
        else:
            possible_pw = ori_pw[0].upper() + ori_pw[1:]
    
    if transformation.find('tail') != -1:
        count -= 1
        if ori_pw[-1].islower():
            possible_pw = ori_pw[:-1] + ori_pw[-1].upper()
        else:
            possible_pw = ori_pw[:-1] + ori_pw[-1].lower()
    
    dfs_change(possible_pw, count, trans_pw, 1)

    return trans_pw
