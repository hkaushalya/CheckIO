__author__ = 'samantha'
def checkio(words):
    #l = list()
    #for word in words.split():
    #    l.append(word.isalpha())
    print(words)
    res = False
    l = [wd.isalpha() for wd in words.split()]
    #r = [l[i:i+3] for i in range(0,len(l)-3)  ]
    #print ('r=',r)
    print ('l=',l)
    if len(l)>3:
        print ('len(l)=', len(l))
        print('range', range(0,len(l)-2))
        for i in range(0,(len(l)-2)):
            print ('i=', i)
            l2 = l[i:i+3]
            print('l2=', l2)
            res = all(x == True for x in l2)
            print ('res=', res)
    elif len(l) == 3:
        res = all(x == True for x in l)

    return res

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
    assert checkio("0 qwerty iddqd asdfg") == True, "0 qwert"
