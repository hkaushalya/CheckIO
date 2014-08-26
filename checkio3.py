import collections

def count_words(text, words):
    count = 0
    if len(text)>0:
        #words = text.lower().split()
        lower_text = text.lower()

    lst = []
    for wd in words:
        if wd in lower_text:
            lst.append(wd)

    count = sum(collections.Counter(lst).values())

    print (count)
    return count


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}) == 3, "Example"
    assert count_words("Bananas, give me bananas!!!", {"banana", "bananas"}) == 2, "BANANAS!"
    assert count_words("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
                      {"sum", "hamlet", "infinity", "anything"}) == 1, "Weird text"

    #tt = 'loren esum gonegone'
    #rd = 'ren'
    #if (rd in tt.split()):
    #    print ('yes')
    #else:
    #    print ('No')