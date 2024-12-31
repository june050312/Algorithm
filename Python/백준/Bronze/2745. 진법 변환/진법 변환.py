from string import ascii_uppercase
alphabet = list(ascii_uppercase)
num, num_sys = input().split()
num = num[::-1]
result = 0
for i in range(len(num)):
    if num[i] in alphabet:
        trans_num = alphabet.index(num[i]) + 10
    else:
        trans_num = int(num[i])
    result += trans_num * (int(num_sys) ** i)
print(result)