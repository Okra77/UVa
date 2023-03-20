while True:
    try:
        s = input().split(' ')
        print(abs(int(s[1]) - int(s[0])))

    except EOFError:
        break