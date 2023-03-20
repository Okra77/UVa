def mul(a:int):
    sum = 0
    while a >  0:
        sum += a % 10
        a //= 10
    return sum

while True:
    try:
        m = int(input())
        if m == 0:break
        while m >= 10:
            m = mul(m)
        print(m)

    except EOFError:
        break