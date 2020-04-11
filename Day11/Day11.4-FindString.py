#S = 'ABCDCDC'
#sub = 'CDC'
#  for i in range(ln_S-ln_Sub+1):
#        if sub_string == string[i:i+ln_Sub]:
#            count+=1
#  ln_Sub = 3
#  Ln_S = 7
#print(S[0:3])
#print(S[1:4])
#print(S[2:5])
#print(S[3:6])
#print(S[4:7])

def count_substring(string, sub_string):
    ln_S = len(string)
    ln_Sub = len(sub_string)
    count = 0
    for i in range(ln_S - ln_Sub + 1):
        if sub_string == string[i:i + ln_Sub]:
            count += 1
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)