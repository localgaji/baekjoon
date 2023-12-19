import sys

# 입력
input = sys.stdin.readline
T = int(input())
answers = [0] * T

# mCn
for t in range(T):
    N, M = map(int, input().split())
    table = [1] * (M + 1)

    for m in range(2, M + 1):
        table[m] = table[m - 1] * m

    answers[t] = table[M] // table[M - N] // table[N]

for a in answers:
    print(a)
