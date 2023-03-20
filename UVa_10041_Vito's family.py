t = int(input())
while t > 0:
    s = list(map(int,input().split(' ')))
    del s[0]
    s.sort()
    sum = 0

    mid = s[len(s)//2]

    for i in range(len(s)):
        sum += abs(mid-s[i])
    print(sum)
       
t -= 1