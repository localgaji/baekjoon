import sys

input = sys.stdin.readline
A, M = map(int, input().split())
memories = list(map(int, input().split()))
costs = list(map(int, input().split()))

C = sum(costs)
dp = [0] * (C + 1)

for a in range(A):
    am, ac = memories[a], costs[a]
    new_dp = dp[:]

    for c in range(ac, C + 1):
        new_dp[c] = max(new_dp[c], dp[c - ac] + am)

    dp = new_dp

for c in range(C + 1):
    if dp[c] >= M:
        print(c)
        break
