def checkio(data):
    print ('len=', len(data))
    print ('len? = ' , len(data)>=10)
    print ('allnum? = ' , data.isnumeric())
    print('allalp? = ' , data.isalpha())

    haslen  = bool(len(data)>=10)
    onedigit = False
    onelower = False
    oneupper = False

    if haslen:
        for c in data:
            if c.isdigit():
                onedigit = True
            elif c.islower():
                onelower = True
            elif c.isupper():
                oneupper = True


    return (len(data)>10 and onedigit and onelower and oneupper)

#Some hints
#Just check all conditions


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
