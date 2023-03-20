a = {}

def cal(x):
    if x in a:
        return a[x]
    if x<=1 :
        return 1
    if x%2==1:
        y=3*x+1
    else:
        y=x//2
    a[x] = cal(y) + 1
    return a[x]



while True:
    try:
        n,m = map(int, input().split(' '))
    except EOFError:
        break

    max_len = 0
    for i in range(min(n,m),max(n,m)+1):
        temp = cal(i)
        if temp > max_len:
            max_len = temp
    print(n,m,max_len)
