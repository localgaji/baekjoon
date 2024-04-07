import sys

input = sys.stdin.readline
N = int(input())
liquids = list(map(int, input().split()))


def search_left(i, x):
    left, right = i, N - 1
    while left <= right:
        center = (left + right) // 2
        if liquids[center] > x:
            right = center - 1
        elif liquids[center] < x:
            left = center + 1
        else:
            return center
    return left


INF = 10 ** 9
optimum = 2 * INF + 1
a, b = -1, -1
for n in range(N):
    aq = liquids[n]
    find_index = search_left(n, -aq)

    for j in range(-1, 1):
        pair_index = find_index + j
        if not 0 <= pair_index < N or pair_index == n:
            continue

        pair = liquids[pair_index]
        mix = abs(aq + pair)

        if mix < optimum:
            optimum = mix
            a, b = aq, pair

    if (n > 0 and liquids[n - 1] > 0) or optimum == 0:
        break

print(*sorted([a, b]))
