import sys

input = sys.stdin.readline
N = int(input())

prev = [0] * (N + 1)
other = [(1, 2), (0, 2), (0, 1)]

for _ in range(N):
    now = list(map(int, input().split()))

    for i in range(3):
        now[i] += min(prev[other[i][0]], prev[other[i][1]])

    prev = now

print(min(prev))
