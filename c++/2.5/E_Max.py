n = int(input())
arr = list(map(int,input().split()))

for i in range(n):
    if arr[0] < arr[i]:
        arr[0] = arr[i]

print(arr[0])