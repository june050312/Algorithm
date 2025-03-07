import sys

input = sys.stdin.readline

dp = [0] * 12
dp[1] = 1
dp[2] = 2
dp[3] = 4
dp[4] = 7
for i in range(5, 12):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for i in range(int(input())):
    print(dp[int(input())])