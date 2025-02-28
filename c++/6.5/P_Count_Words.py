s = input()
count = 0
word = False

for char in s:
    if('a' <= char <= 'z' or 'A' <= char <= 'Z'):
        if not word:
            count += 1
            word = True
    else:
        word = False


print(count)