numbers = [0, 0]

print(str(int("".join(sorted(list(map(str, numbers)), key=lambda x : x*3, reverse=True)))))