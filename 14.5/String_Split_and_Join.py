def split_and_join(line):
    # write your code here
    return '-'.join(line)

if __name__ == '__main__':
    line = input().split(" ")

    joined = split_and_join(line)
    print(joined)