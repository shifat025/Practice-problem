n = int(input())
country = set()

for i in range(n):
    stamp = input()
    country.add(stamp)

print(len(country))