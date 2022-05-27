n, t = map(int, input().split())  
# n = kol-vo sotrudnikov, t = vremya uhoda sotr
etagi = list(map(int, input().split()))
sotr = int(input())
a = 0
# a = min kolvo proletov

if (etagi[sotr-1]  - etagi[0] <= t) or (etagi[n-1] - etagi[sotr-1] <=t):
     print(etagi[n-1] - etagi[0])
else:
    if etagi[sotr-1] - etagi[0] > etagi[n-1] - etagi[sotr-1]:
        print((etagi[n-1] - etagi[sotr-1]) * 2 + etagi[sotr-1] - etagi[0])
    else:
        print((etagi[sotr-1] - etagi[0])*2 + etagi[n-1] - etagi[sotr-1])
