def letter_queue(commands):
    q = list()
    for c in commands:
        if "PUSH" in c:
            q.append(c[-1])
        elif "POP" in c:
            if len(q)>0:
                q.pop(0)        
    return "".join(q)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    print(letter_queue(["PUSH A", "POP", "POP", "PUSH Z", "PUSH D", "PUSH O", "POP", "PUSH T"]))
    assert letter_queue(["PUSH A", "POP", "POP", "PUSH Z", "PUSH D", "PUSH O", "POP", "PUSH T"]) == "DOT", "dot example"
    assert letter_queue(["POP", "POP"]) == "", "Pop, Pop, empty"
    assert letter_queue(["PUSH H", "PUSH I"]) == "HI", "Hi!"
    assert letter_queue([]) == "", "Nothing"
