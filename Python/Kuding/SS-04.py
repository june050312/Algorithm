N = 4
stages = [4,4,4,4,4]

player = len(stages)
failRate = {}
for i in range(1, N+1):
    if player == 0:
        failRate[i] = 0.0
    else:
        failRate[i] = stages.count(i) / player
        player -= stages.count(i)
failRate = sorted(failRate.items(), key=lambda x : x[1], reverse=True)
answer = []
for i in failRate:
    answer.append(i[0])
print(answer)