import itertools

a = int(input())
b = list(map(int, input().split()))[:3]
k = 0
for j in range(100):
    for i in list(itertools.combinations_with_replacement(b,j)):
        if sum(i) < a:
            k += 1
            # print(i, type(i))

print(k)
