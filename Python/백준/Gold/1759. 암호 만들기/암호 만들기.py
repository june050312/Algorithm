import sys, itertools

input = sys.stdin.readline

pwLen, c = map(int, input().split())
pwWord = list(input().split())

# 모음, 자음 구분
vowel = []
consonant = []
for word in pwWord:
    if word in ['a', 'e', 'i', 'o', 'u']:
        vowel.append(word)
    else:
        consonant.append(word)
vowel = list(set(vowel))
consonant = list(set(consonant))

# 비밀번호 만들기
# 1. 모음으로 할 수 있는 모든 경우의 수 제작
# 2. 모음에 따른 자음으로 할 수 있는 모든 경우의 수 제작
# 3. 두 리스트를 합쳐 사전 순으로 정렬
vowel.sort()
vowelList = []
vowelSize = len(vowel)

# 1
for size in range(vowelSize):
    vowelList.append(list(itertools.combinations(vowel, size + 1)))

# 2
consonantList = []
for size in range(vowelSize):
    consonantList.append(list(itertools.combinations(consonant, pwLen - size - 1)))

# 3
result = []
consonantSize = len(consonantList)
# 모음 처리
for numOfVowel in range(vowelSize):
    for vowelWord in vowelList[numOfVowel]:
        # 자음 처리
        for consonantWord in consonantList[numOfVowel]:
            if len(consonantWord) > 1:
                prePw = " ".join(vowelWord) + " " + " ".join(consonantWord)
                editPw = "".join(sorted(prePw.split()))
                result.append(editPw)
            else:
                continue

result.sort()
for i in result:
    print(i)