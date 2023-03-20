def convert(x):
    if(x>=10000000):
        convert(x//10000000)
        x%=10000000
        print(' kuti', end='')
    if(x>=100000):
        convert(x//100000)
        x%=100000
        print(' lakh', end='')
    if(x>=1000):
        convert(x//1000)
        x%=1000
        print(' hajar', end='')
    if(x>=100):
        convert(x//100)
        x%=100
        print(' shata', end='')
    if(x):
        print(' {}'.format(x), end='')
    return ''
case = 0
while True:
    try:
        case += 1
        n = int(input())
        print('{0:>4}.'.format(case), end='')
        print(convert(n))
    except EOFError:
        break