t = "3141592"
p = "271"

cnt = 0
for i in range(len(t) - len(p) + 1):
    if int(p) >= int(t[i:i+len(p)]):
        cnt += 1
print(cnt)