import sys

input = sys.stdin.readline
N = int(input())

max_bit = 2 ** 10 - 1
binary = [0] * (max_bit + 1)
dp = [[binary[:] for _ in range(10)] for _ in range(N + 1)]

for k in range(1, 10):
    dp[1][k][2 ** k] = 1

for n in range(2, N + 1):
    for k in range(10):
        for bit in range(max_bit + 1):
            new_bit = bit | 2 ** k
            if k > 0:
                dp[n][k][new_bit] += dp[n - 1][k - 1][bit]
            if k < 9:
                dp[n][k][new_bit] += dp[n - 1][k + 1][bit]

answer = 0
for k in range(10):
    answer += dp[N][k][max_bit]
print(answer % (10 ** 9))
