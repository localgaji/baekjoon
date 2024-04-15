import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
origin = [list(map(int, input().split())) for _ in range(N)]
maximum = [0]


def dfs(count, board):
    if count == 5:
        maximum_block = 0
        for row in board:
            if max(row) > maximum_block:
                maximum_block = max(row)
        maximum[0] = max(maximum_block, maximum[0])
        return

    for nd in range(4):
        new_board = move(nd, board)
        dfs(count + 1, new_board)


def move(d, before):
    after = [row[:] for row in before]

    if d % 2 == 0:
        s, e, v = 0, N, 1
    else:
        s, e, v = N - 1, -1, -1

    # 상, 하
    if d <= 1:
        for c in range(N):
            new_row = deque()
            last = 0
            for r in range(s, e, v):
                if after[r][c] == 0:
                    continue
                if last == after[r][c]:
                    new_row.append(last * 2)
                    last = 0
                else:
                    if last > 0:
                        new_row.append(last)
                    last = after[r][c]
            if last > 0:
                new_row.append(last)

            for r in range(s, e, v):
                if new_row:
                    after[r][c] = new_row.popleft()
                else:
                    after[r][c] = 0

    # 좌, 우
    else:
        for r in range(N):
            new_row = deque()
            last = 0
            for c in range(s, e, v):
                if after[r][c] == 0:
                    continue
                if last == after[r][c]:
                    new_row.append(last * 2)
                    last = 0
                else:
                    if last > 0:
                        new_row.append(last)
                    last = after[r][c]
            if last > 0:
                new_row.append(last)

            for c in range(s, e, v):
                if new_row:
                    after[r][c] = new_row.popleft()
                else:
                    after[r][c] = 0

    return after


dfs(0, origin)
print(maximum[0])
