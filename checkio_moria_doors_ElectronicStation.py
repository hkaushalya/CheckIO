def find_word(message):
    words = message.lower().split()
    wd = ""
    mws = 0     #score of matched
    for w1 in words:
        score = 0.0
        for w2 in words:
            print ("%s -> %s -> %f" % (w1, w2, score))
            l1 = len(w1)
            l2 = len(w2)
            if l1>0 and l2>0:
                if (w1[0] == w2[0]):        # same first
                    score += 0.1
                print("A score = %f" % score)
                if (w1[-1] == w2[-1]):      # same last
                    score += 0.1
                print("B score = %f" % score)
                
                if l1 <= l2:                # length comparison
                    score += 0.3 * l1 / l2
                else:
                    score += 0.3 * l2 / l1
                print("C score = %f" % score)

                #uniqueness
                s1 = set(w1)
                s2 = set(w2)
                score += 0.5 * len(s1.union(s2)) / len(s1.intersection(s2))
                print("D score = %f" % score)

        #avg score
        score = score / len(words)
        print("E score = %f" % score)
                   
        if score > mws:
            wd = w1
            mws = score

    print("%s -> %f" % (wd, mws) )
    
    return ""

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    find_word("Speak friend and enter.")
    #assert find_word("Speak friend and enter.") == "friend", "Friend"
