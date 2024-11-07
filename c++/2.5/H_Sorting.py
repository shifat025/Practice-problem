n = int(input())
A = list(map(int,input().split()))

for i in range(0,n-1):
    for j in range(0,n-i-1):
        if A[j] > A[j+1]:
            tmp = A[j]
            A[j] = A[j+1]
            A[j+1] = tmp
            

for i in range(n):
    if i == n - 1:
        print(A[i])  # Print last element without trailing space
    else:
        print(A[i], end=" ")