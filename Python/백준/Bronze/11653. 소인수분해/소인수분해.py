num = int(input())
prime_num = 2
while num > 1:
    if num % prime_num == 0:
        num /= prime_num
        print(prime_num)
    else:
        prime_num += 1