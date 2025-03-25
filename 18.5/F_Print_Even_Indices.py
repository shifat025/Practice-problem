n = int(input())
m = list(map(int, input().split()))

even_indexed = []
for i in range(n):
    if i%2 == 0:
        even_indexed.append(m[i])

print(' '.join(map(str, reversed(even_indexed))))
    

