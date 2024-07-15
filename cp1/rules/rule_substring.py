def check_substring(pw1,pw2):
    #pw1,pw2 (string,string): a pair of input password
    #output (boolean): if pw1 and pw2 can be considered as substring of the other 
    # eg. pw1 = abc, pw2 = abcd, output true
    # eg. pw1 = abcde, pw2 = abcd, output true

    # ***********************************************************************
    # ****************************** TODO ***********************************
    # ***********************************************************************

    if pw2 in pw1 or pw1 in pw2:
        return True

    return False

def check_substring_transformation(pw1, pw2):
    #pw1,pw2 (string,string): a pair of input password
    #output (string): transformation between pw1 and pw2
    #example: pw1=123hello!!, pw2=hello, output=head\t123\ttail\t!!
    #example: pw1=hello!!, pw2=hello, output=head\t\ttail\t!!

    # ***********************************************************************
    # ****************************** TODO ***********************************
    # ***********************************************************************

    outputStr = ''

    if pw2 in pw1:
        pos = pw1.find(pw2)
        outputStr = 'head\t' + pw1[:pos] + '\ttail\t' + pw1[pos+len(pw2):]

    elif pw1 in pw2:
        pos = pw2.find(pw1)
        outputStr = 'head\t' + pw2[:pos] + '\ttail\t' + pw2[pos+len(pw1):]


    return outputStr

def guess_target_as_substring(ori_pw):
    #the first transformation applied in rule_substring
    #guess the possible passwords as a substring
    #decide to only consider the substring from head or from tail
    #e.g. pw1=abc123, output = [a,ab,abc,abc1,abc12,3,23,123,c123,bc123]
    #in transformation dictionary, the transformation = 'special_trans_as_substring'

    # ***********************************************************************
    # ****************************** TODO ***********************************
    # ***********************************************************************


    guess_pw = []
    for i in range(len(ori_pw) - 1):
        guess_pw.append(ori_pw[:i+1])
        guess_pw.append(ori_pw[i+1:])

    return guess_pw

def apply_substring_transformation(ori_pw, transformation):
    #ori_pw (string): input password that needs to be transformed
    #transformation (string): transformation in string
    #output (list of string): list of passwords that after transformation
    #add head string to head, add tail string to tail
    
    # ***********************************************************************
    # ****************************** TODO ***********************************
    # ***********************************************************************

    trans_pw = []
    if transformation == 'special_trans_as_substring':
        trans_pw = guess_target_as_substring(ori_pw)
    else:
        tailPos = transformation.find('\ttail\t')
        headPos = transformation.find('head\t')
        
        tail = transformation[tailPos+6:]
        head = transformation[headPos+5:tailPos]
       
        trans_pw.append(head + ori_pw + tail)

    return trans_pw