N = int(input())
A = []

for i in range(N):
    row = list(map(int,input().split()))
    A.append(row)

for row in A:
    for i in range(len(row)):
        # Print the element followed by a space, except for the last element
        if i == len(row) - 1:
            print(row[i], end="")  # Don't print a space after the last element
        else:
            print(row[i], end=" ")
    # Move to the next line after printing each row
    print()