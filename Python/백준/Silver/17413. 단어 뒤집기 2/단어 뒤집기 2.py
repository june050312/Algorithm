import sys
sen = sys.stdin.readline().strip()
temp = []
trg = False
for i in sen:
    if i == '<':
        print(''.join(temp[::-1]), end = '')
        temp = []
        trg = True
    
    if trg:
        print(i, end = '')
        if i == '>':
            trg = False
    elif i == ' ':
        print(''.join(temp[::-1]), end = ' ')
        temp = []
    else:
        temp.append(i)
print(''.join(temp[::-1]))