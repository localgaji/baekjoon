import sys

# 입력
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
T = int(input())


def find_root(x):
    if x not in roots:
        roots[x] = x
        children[x] = 1
    if roots[x] != x:
        roots[x] = find_root(roots[x])
    return roots[x]


def union(x, y):
    root_x, root_y = find_root(x), find_root(y)
    big, small = root_x, root_y
    if small > big:
        big, small = small, big

    if roots[big] == small:
        return

    children[small] += children[big]
    roots[big] = small
    find_root(big)


for _ in range(T):
    N = int(input())
    roots = dict()
    children = dict()

    for _ in range(N):
        a, b = input().split()
        union(a, b)
        root = find_root(b)

        print(children[root])
