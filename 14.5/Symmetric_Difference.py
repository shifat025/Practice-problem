# Step 1: Read the inputs
m = int(input())  # Size of set a (not needed, but read as per input format)
a = set(map(int, input().split()))  # Set a

n = int(input())  # Size of set b (not needed, but read as per input format)
b = set(map(int, input().split()))  # Set b

# Step 2: Calculate the symmetric difference
sym_diff = a.symmetric_difference(b)  # Or equivalently: a ^ b

# Step 3: Sort the symmetric difference
sorted_sym_diff = sorted(sym_diff)

# Step 4: Print each element in the sorted symmetric difference
for element in sorted_sym_diff:
    print(element)
