l, r = map(int, input().split())
lr = range(l, r+1)
k = 0

for n in lr:
    lastNum = n % 10
    num = lastNum
    while n != 0 and num == lastNum:
        num = n % 10
        n = n // 10
    if num == lastNum:
        k += 1
print(k)
