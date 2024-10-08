import sys

input = sys.stdin.readline

trees = {}
cnt = 0
while True:
    tree = input().strip()
    if tree:
        cnt += 1
        if tree in trees:
            trees[tree] += 1
        else: 
            trees[tree] = 1
    else:
        break

for tree in trees:
    trees[tree] = ((trees[tree] / cnt) * 100)

trees_list = sorted(trees.items())
for tree in trees_list:
    print(tree[0], f'{tree[1]:.4f}')