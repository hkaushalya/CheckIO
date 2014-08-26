def checkio(array):
    """
        sums even-indexes elements and multiply at the last
    """
    res = 0
    if len(array)>0:
        sum = 0
        for i in range(0,len(array)):
            if i % 2 == 1:
                continue
            print ('Selecting ', i , '->', array[i])
            sum += array[i]

        print ('Last item = ', array[-1])
        res = sum * array[-1]
        print (array, '->', res,'\n\n')

    return res

def checkio2(array):
    """
        sums even-indexes elements and multiply at the last
    """
lambda array: sum(array[::2]) * sum(array[-1:])

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    #assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    #assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
    #assert checkio([6]) == 36, "(6)*6=36"
    assert checkio2([]) == 0, "An empty array = 0"