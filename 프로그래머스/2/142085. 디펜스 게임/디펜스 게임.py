import heapq


def solution(n, k, enemy):
    left = n
    q = []

    for r, e in enumerate(enemy):
        heapq.heappush(q, -e)
        left -= e

        while left < 0 and k > 0:
            maximum = -heapq.heappop(q)
            left += maximum
            k -= 1

        if k == 0 and left < 0:
            return r

    return len(enemy)