def balanced(s):
    x = 0
    y = 0
    for i in range(len(s)):
        if s[i] == 'x':
            x+=1
        if s[i] == 'y':
            y+=1
    if x == y:
        return True
    return False


def balanced_bonus(s):
    letterDict = {}
    if s == '':
        return True
    for i in range(len(s)):
        if letterDict.get(s[i]) is None:
            letterDict[s[i]] = 1
        else:
            letterDict[s[i]] = letterDict.get(s[i]) + 1
    finalCounts = [letterDict.get(letter)for letter in letterDict.keys()]
    if len(set(finalCounts)) == 1:
        return True
    return False


def main():
    print 'Test 1' , bool(balanced("xxxyyy") == True)
    print 'Test 2', bool( balanced("yyyxxx") == True)
    print 'Test 3', bool(balanced("xxxyyyy") == False)
    print 'Test 4', bool(balanced("yyxyxxyxxyyyyxxxyxyx") == True)
    print 'Test 5', bool(balanced("xyxxxxyyyxyxxyxxyy") == False)
    print 'Test 6', bool(balanced("") == True)
    print 'Test 7', bool( balanced("x") == False)
    print 'Bonus Test 1' , bool(balanced_bonus("xxxyyyzzz") == True)
    print 'Bonus Test 2' , bool(balanced_bonus("abccbaabccba") == True)
    print 'Bonus Test 3' , bool(balanced_bonus("xxxyyyzzzz") == False)
    print 'Bonus Test 4' , bool(balanced_bonus("abcdefghijklmnopqrstuvwxyz") == True)
    print 'Bonus Test 5' , bool(balanced_bonus("pqq") == False)
    print 'Bonus Test 6' , bool(balanced_bonus("fdedfdeffeddefeeeefddf") == False)
    print 'Bonus Test 7' , bool(balanced_bonus("www") == True)
    print 'Bonus Test 8' , bool(balanced_bonus("x") == True)
    print 'Bonus Test 9' , bool(balanced_bonus("") == True)


if __name__ == '__main__':
    main()



