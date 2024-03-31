import sys

sys.setrecursionlimit(10**9)
input = sys.stdin.readline
N = int(input())
memo = dict()
memo[0], memo[1] = 0, 1
DIV = 1000000007


def recursive(n):
    if n in memo:
        return memo[n]
    half = recursive(n // 2)

    if n % 2 == 1:
        memo[n] = (half ** 2 + recursive(n // 2 + 1) ** 2) % DIV
        return memo[n]

    memo[n] = half * (half + 2 * recursive(n // 2 - 1)) % DIV
    return memo[n]


print(recursive(N))
