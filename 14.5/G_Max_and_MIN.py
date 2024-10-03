def min_max(a):
    min_number = min(a)
    max_number = max(a)
    return min_number,max_number

a = int(input())
b = list(map(int, input().split()))

min_number, max_number = min_max(b)

# Output: Print the result
print(min_number, max_number)