S = input().split()

result = ""

for word in S:
    reversed_word = ""

    for char in word:
        reversed_word = char + reversed_word
        
    if result:
        result += " " + reversed_word

    else:
        result = reversed_word

print(result)