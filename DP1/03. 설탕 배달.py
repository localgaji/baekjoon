import sys

# 입력
input = sys.stdin.readline
N = int(input())

# 탐색
table = [-1] * (N + 1)
table[0] = 0

for n in range(3, N + 1):
    new = []

    if table[n - 5] != -1:
        new.append(table[n - 5])

    if table[n - 3] != -1:
        new.append(table[n - 3])

    if new:
        table[n] = min(new) + 1

print(table[N])
