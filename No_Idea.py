import sys
input = sys.stdin.read
data = input().splitlines()

# Read integers n and m
n, m = map(int, data[0].split())

# Read the array of integers
array = list(map(int, data[1].split()))

# Read liked and disliked sets
set_A = set(map(int, data[2].split()))
set_B = set(map(int, data[3].split()))

happienes = 0
for i in array:
    if i in set_A:
        happienes += 1
    elif i in set_B:
        happienes -= 1

print(happienes)


