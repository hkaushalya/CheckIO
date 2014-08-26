from __future__ import division # to pull python 3.0 for division
import math

def checkio(data):
    print (data)
    new_data = sorted(data)
    print ('new_data = ' , new_data)
    size = len(new_data)
    print ('size =', size)

    print (size%2)
    if size%2 == 0:
        ind = math.floor(size/2)
        med = (new_data[ind-1] + new_data[ind])/ float(2)
        print ('in there')
    else:
        ind = math.ceil(size/2)
        med = new_data[ind-1]

    print ('med = ', med)
    return med

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
   # assert checkio([1, 2, 3, 4, 5]) == 3, "Sorted list"
    assert checkio([3, 1, 2, 5, 3]) == 3, "Not sorted list"
    assert checkio([1, 300, 2, 200, 1]) == 2, "It's not an average"
    assert checkio([3, 6, 20, 99, 10, 15]) == 12.5, "Even length"
    print("Start the long test")
    assert checkio(list(range(1000000))) == 499999.5, "Long."
    print("The local tests are done.")