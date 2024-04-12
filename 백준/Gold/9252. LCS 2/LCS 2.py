import sys

input = sys.stdin.readline
A = input().rstrip()
B = input().rstrip()

dp = [""] * (len(B) + 1)

for a in range(len(A)):
    sa = A[a]
    new_dp = [""] * (len(B) + 1)

    for b in range(1, len(B) + 1):
        sb = B[b - 1]

        if sa == sb:
            new_dp[b] = dp[b - 1] + sa
        else:
            if len(dp[b]) > len(new_dp[b - 1]):
                new_dp[b] = dp[b]
            else:
                new_dp[b] = new_dp[b - 1]
    dp = new_dp

print(len(dp[-1]))
if len(dp[-1]) > 0:
    print(dp[-1])
