while True:
    try:
        m = list(map(int,input().split()))
        m.pop(0)
        temp = [0 for i in range(3001)]

        for i in range(1,len(m)):
            n = abs(m[i]-m[i-1])
            if temp[n] == 0 and n < len(m): temp[n] = 1

        if sum(temp) == len(m) - 1:
            print('Jolly')
        else:
            print('Not jolly')


    except EOFError:
        break