import sys

# 입력
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
T = int(input())


def find_root(x):
    if x not in roots:
        roots[x] = x
        counts[x] = 1
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
    counts[root_y] += counts[root_x]


for _ in range(T):
    F = int(input())
    roots = {}
    counts = {}

    for _ in range(F):
        a, b = input().split()
        union(a, b)
        root_a = find_root(a)
        print(counts[root_a])
