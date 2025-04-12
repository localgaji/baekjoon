import sys
from collections import deque

# 입력
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())
graph: list[list[int]] = [[] for _ in range(N + 1)]
enter = [0] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    enter[b] += 1


def topology_sort(root):
    q = deque([(root, answer[root])])
    
    while q:
        # 큐에 담긴 노드를 꺼내어
        now, order = q.popleft()

        # 노드에서 출발하는 모든 간선을 제거
        for arrival in graph[now]:
            enter[arrival] -= 1
            answer[arrival] = max(answer[arrival], order + 1)

            # 진입 차수가 0이면 큐에 넣기
            if enter[arrival] == 0:
                q.append((arrival, answer[arrival]))

        graph[now] = []


answer = [1] * (N + 1)
for n in range(1, N + 1):
    if enter[n] > 0:
        continue
    topology_sort(n)

print(*answer[1:])
