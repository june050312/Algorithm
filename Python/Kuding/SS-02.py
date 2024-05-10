n = 118372

arr = []
for i in str(n):
    arr.append(i)
print(int("".join(sorted(arr, reverse=True))))
