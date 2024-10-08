word = input()
strList = []
for length in range(len(word)):
    for start in range(len(word) - length):
        strList.append(word[start : start + length + 1])
strList = list(set(strList))
print(len(strList))