import sys
input = sys.stdin.readline

def bfs(init):
    q = []
    visited = [0] * (height + 1)

    q.append(init)
    visited[init] = 1

    while q:
        cur_floor = q.pop(0)

        if cur_floor == startlink_floor:
            return visited[cur_floor] - 1

        for dir in [up, -down]:
            next_floor = cur_floor + dir

            if 1 <= next_floor <= height and visited[next_floor] == 0:
                q.append(next_floor)
                visited[next_floor] = visited[cur_floor] + 1
    return "use the stairs"

height, start_floor, startlink_floor, up, down = map(int, input().split())

print(bfs(start_floor))