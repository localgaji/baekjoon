import heapq
import sys


def dijkstra(start, end):
    distances = [INF] * (V + 1)
    distances[start] = 0
    pq = [(0, start)]

    while pq:
        cost, now = heapq.heappop(pq)
        if cost > distances[now]:
            continue

        for near, now_near in graph[now]:
            start_near = cost + now_near

            if start_near < distances[near]:
                distances[near] = start_near
                heapq.heappush(pq, (start_near, near))

    return distances[end]


input = sys.stdin.readline
V, E = map(int, input().split())
graph: list[list[tuple[int, int]]] = [[] for _ in range(V + 1)]

for _ in range(E):
    s, e, c = map(int, input().split())
    graph[s].append((e, c))
    graph[e].append((s, c))

v1, v2 = map(int, input().split())
INF = 10 ** 9


def total_cost(u, v):
    a = dijkstra(1, u)
    b = dijkstra(u, v)
    c = dijkstra(v, V)

    if INF in [a, b, c]:
        return -1

    return a + b + c


x = total_cost(v1, v2)
y = total_cost(v2, v1)
if x >= INF and y >= INF:
    print(-1)
else:
    print(min(x, y))
