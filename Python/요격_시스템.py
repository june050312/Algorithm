targets = [[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]

targets.sort(key = lambda x : (x[1], x[0]))

cnt = 0
end = 0
for target in targets:
    if (target[0] >= end):
        cnt += 1
        end = target[1]

print(cnt)