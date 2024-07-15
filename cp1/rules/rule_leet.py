import itertools

#a more complete leet_list
#leet_list = [{'4', 'a', '@', '/\\', '/-\\'}, {'b', '|3', '8', '|o'}, {'<', 'K', 'g', 'S', '9', '6', 'c', '('}, {'0', '()', '{}', 'o', '[]'}, {'!', '|', '][', '#', ')-(', '1', 'i', 'l', '}-{', '|-|', '+', 't', ']-[', 'h', '(-)', '7'}, {'5', 's', '$'}, {'+', 't'}, {'/\\/\\', 'm', '/v\\', '/|\\', '/\\\\', '|\\/|', '(\\/)', "|'|'|"}, {'\\|/', '\\|\\|', '\\^/', '//', 'w', '|/|/', '\\/\\/'}, {'|\\|', '|\\\\|', 'n', '/|/', '/\\/'}, {'u', '|_|'}, {'2', '(\\)', 'z'}, {'(,)', 'q', 'kw'}, {'v', '|/', '\\|', '\\/', '/'}, {'k', '/<', '|{', '\\<', '|<'}, {'<|', 'o|', '|)', '|>', 'd'}, {'f', 'ph', '|=', 'p#'}, {'l', '|_'}, {'j', 'y', '_|'}, {'}{', 'x', '><'}, {"'/", 'y', '`/'}, {'p', '|D', 'r', '|2'}, {'r', '|Z', '|?'}, {'e', '3'}]
leet_list = [{"@","a"},{"3","e"},{"1","i"},{"0","o"},{"$","s"},{"+","t"},{"4","a"},{"5","s"},{"|","i"},{"!","i"}]


def dfs_leet(pw, res, pos, leetPairs):
    if pos == len(leetPairs):
        res.append(pw)
        return

    A = leetPairs[pos][0]
    b = leetPairs[pos][1]

    # A -> b
    posA = []
    pA = pw.find(A)
    while pA != -1:
        posA.append(pA)
        pA = pw.find(A, pA + 1)
    
    for i in range(len(posA)):
        dfs_leet(pw[:posA[i]] + b + pw[posA[i] + 1:], res, pos + 1, leetPairs)

    # b -> A
    posb = []
    pb = pw.find(b)
    while pb != -1:
        posb.append(pb)
        pb = pw.find(b, pb + 1)
    
    for i in range(len(posb)):
        dfs_leet(pw[:posb[i]] + A + pw[posb[i] + 1:], res, pos + 1, leetPairs)

def check_leet(pw1,pw2):
    #pw1,pw2 (string,string): a pair of input password
    #output (boolean): if pw1 and pw2 can be transformed by this category of rule
    #e.g. pw1 = abcde, pw2 = @bcd3 , output = True
    
    # ***********************************************************************
    # ****************************** TODO ***********************************
    # ***********************************************************************

    if len(pw2) != len(pw1):
        return False
    
    for i in range(len(pw1)):
        if pw2[i] != pw1[i]:
            flag = False
            for j in range(len(leet_list)):
                leetPair = list(leet_list[j])
                if pw1[i] == leetPair[0]:
                    if pw2[i] == leetPair[1]:
                        flag = True
                        break
                elif pw1[i] == leetPair[1]:
                    if pw2[i] == leetPair[0]:
                        flag = True
                        break
            if flag == False:
                return False

    return True

def check_leet_transformation(pw1, pw2):
    #pw1,pw2 (string,string): a pair of input password
    #output (string): transformation between pw1 and pw2
    #example: pw1=abcd3 pw2 = @bcde, transformation = 3e\ta@ because pw1->pw2:3->e and a->@ and '3e'<'a@' for the order
    #for simplicity, duplicate item is allowed. example: pw1=abcda pw2 = @bcd@, transformation = a@\ta@ 
    
    # ***********************************************************************
    # ****************************** TODO ***********************************
    # ***********************************************************************

    leetPairs = []
    outputStr = ''
    

    for i in range(len(pw1)):
        if pw1[i] != pw2[i]:
            leetPairs.append(str(pw1[i] + pw2[i]))
    
    leetPairs = sorted(leetPairs)

    for i in range(len(leetPairs)):
        if i == len(leetPairs) - 1:
            outputStr += leetPairs[i]
        else:
            outputStr += leetPairs[i] + '\t'

    return outputStr


def apply_leet_transformation(ori_pw, transformation):
    #ori_pw (string): input password that needs to be transformed
    #transformation (string): transformation in string
    #output (list of string): list of passwords that after transformation
    #only need to consider forward transformation and backward transformation combinations.
    #forward transformation: each term in transformation, can be and only be applied once on the ori_pw in forward direction (3->e,a->@)
    #backward: (e->3,@->a)
    
    # ***********************************************************************
    # ****************************** TODO ***********************************
    # ***********************************************************************
    
    trans_pw = []
    leetPairs = transformation.split('\t')

    dfs_leet(ori_pw, trans_pw, 0, leetPairs)

    return trans_pw
