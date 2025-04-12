import sys

# 입력
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N, M = map(int, input().split())


def find_root(x):
    if x != roots[x]:
        roots[x] = find_root(roots[x])
    return roots[x]


def union(x, y):
    root_x = find_root(x)
    root_y = find_root(y)

    if root_x == root_y:
        return
    if root_x > root_y:
        root_x, root_y = root_y, root_x

    roots[root_x] = root_y


roots = [i for i in range(N + 1)]
answer = {True: "YES", False: "NO"}

for _ in range(M):
    q, a, b = map(int, input().split())
    if not q:
        union(a, b)
    else:
        print(answer[find_root(a) == find_root(b)])
