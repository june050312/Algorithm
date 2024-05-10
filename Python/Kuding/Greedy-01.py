n = 5
lost = [1,2]
reserve = [2,3]

newLost = set(lost) - set(reserve)
newReserve = set(reserve) - set(lost)
for i in newLost:
    if i - 1 in newReserve:
        newReserve.remove(i - 1)
    elif i + 1 in newReserve:
        newReserve.remove(i + 1)
    else:
        n -= 1
print(n)