amount, limit = map(int, input().split())
number = list(map(int, input().split()))
new_num = 0
for i in range(amount):
    for j in range(i, amount):
        for k in range(j, amount):
            if number[i] + number[j] + number[k] <= limit and new_num < number[i] + number[j] + number[k] and number[i] != number[j] != number[k]:
                new_num = number[i] + number[j] + number[k]
print(new_num)