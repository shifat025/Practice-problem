n = int(input())

tens_unit = n//10
units_digit = n%10

if units_digit != 0 and tens_unit%units_digit==0 :
    print('YES')
elif tens_unit != 0 and units_digit%tens_unit==0:
    print('YES')
else:
    print('NO')