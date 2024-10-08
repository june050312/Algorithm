import sys

input = sys.stdin.readline

num_amount = int(input())
nums = []

# 최빈값
cnt = {}

for _ in range(num_amount):
    num = int(input())
    nums.append(num)

    if num not in cnt:
        cnt[num] = 1
    else:
        cnt[num] += 1

nums.sort()

# 산술평균
print(int(((sum(nums) / num_amount) + 0.5) // 1))

# 중앙값
print(nums[(num_amount - 1) // 2])

# 최빈값
mode = []
max_cnt = max(cnt.values())
for key, val in cnt.items():
    if val == max_cnt:
        mode.append(key)

if len(mode) == 1:
    print(*mode)
else:
    mode.sort()
    print(mode[1])

# 범위
print(nums[-1] - nums[0])