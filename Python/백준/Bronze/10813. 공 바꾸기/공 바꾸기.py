quantity, repeat = map(int, input().split(' '))

basket = []
for i in range(quantity):
    basket.append(i + 1)

for i in range(repeat):
    basket1, basket2 = map(int, input().split(' '))
    ball1 = basket[basket1 - 1]
    ball2 = basket[basket2 - 1]
    basket[basket1 - 1] = ball2
    basket[basket2 - 1] = ball1

print(*basket)