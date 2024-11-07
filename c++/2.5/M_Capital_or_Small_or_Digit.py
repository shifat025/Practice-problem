X = ord(input())

if(X >= 65 and X <= 95):
    print("ALPHA")
    print("IS CAPITAL")

elif(97 <= X <= 122):
    print("ALPHA")
    print("IS SMALL")

else:
    print("IS DIGIT")