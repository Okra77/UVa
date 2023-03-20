a = {}

n = int(input())
for i in range(n):
    m = list(input().split())
    if m[0] not in a :
        a[m[0]] = 1
    else :
        a[m[0]] += 1
b = sorted(a)
for i in b:
    print("{} {}".format(i,a[i]))