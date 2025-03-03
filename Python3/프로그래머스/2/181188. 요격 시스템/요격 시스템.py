def solution(targets):
    targets.sort(key = lambda x : (x[1], x[0]))

    cnt = 0
    end = 0
    for target in targets:
        if (target[0] >= end):
            cnt += 1
            end = target[1]

    return cnt