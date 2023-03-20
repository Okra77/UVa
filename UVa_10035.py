while True:
        x,y = map(int,input().split(' '))
        if x == 0 and y == 0:
            break
        sum = 0
        k = 0 #進位判斷

        while x!= 0 and y != 0:
            if x%10 + y%10 + k >= 10:
                sum += 1
                k = 1
            else:
                k = 0
            x //= 10
            y //= 10

        if sum == 0:
             print('No carry operation.')
        elif sum == 1:
             print('1 carry operation.')
        else:
             print('{} carry operations.'.format(sum))

            
            