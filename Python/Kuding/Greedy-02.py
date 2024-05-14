number = "4177252841"
k = 4

answer = []
for i, num in enumerate(number):
    while len(answer) > 0 and k > 0 and answer[-1] < num:
        answer.pop()
        k -= 1
    if k == 0:
        answer += list(number[i:])
        break
    answer.append(num)
answer = answer[:-k] if k > 0 else answer
print("".join(answer))