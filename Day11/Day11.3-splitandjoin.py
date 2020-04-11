def split_and_join(line):
    S = line.split()
    S = "-".join(S)
    return S

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)