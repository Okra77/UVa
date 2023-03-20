while True:
    try:
        c = [0 for i in range(26)]
        d = [0 for i in range(26)]
        a,b = input(),input()

        for i in a:
            c[ord(i)-97] += 1
        for i in b:
            d[ord(i)-97] += 1

        for i in range(26):
            if c[i] > 0 and d[i] > 0:
                print(chr(i+97),end='')
        print() 

    except EOFError:
        break