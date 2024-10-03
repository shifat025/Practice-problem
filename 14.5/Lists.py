if __name__ == '__main__':
    N = int(input())
    lst = []
    
    for i in range(N):
        types = input().split()
        
        if types[0] == 'insert':
            index = int(types[1])
            value = int(types[2])
            lst.insert(index,value)
        elif types[0] == 'print':
            print(lst)
        elif types[0] == 'remove':
            lst.remove(int(types[1]))
        elif types[0] == 'append':
            lst.append(int(types[1]))
        elif types[0] == 'sort':
            lst.sort()
        elif types[0] == 'pop':
            lst.pop()
        elif types[0] == 'reverse':
            lst.reverse()
       

