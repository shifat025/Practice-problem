def number(a):
    numbers = []
    for num in range(1,a+1):
        numbers.append(num)
    return numbers
    

a = int(input())
nu = number(a)

print(*nu)


