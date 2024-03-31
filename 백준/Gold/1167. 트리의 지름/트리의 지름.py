import sys

input = sys.stdin.readline
V = int(input())
graph = [[] for _ in range(V + 1)]
for _ in range(V):
    data = list(map(int, input().split()))
    node = data[0]
    for i in range(1, len(data) - 1, 2):
        graph[node].append((data[i], data[i + 1]))


def search_length(root):
    visited = [0] * (V + 1)
    visited[root] = 1

    farthest = 0

    def dfs(now, total):
        max_sub = 0
        deepest_leaf = now
        for near, now_near in graph[now]:
            if visited[near]:
                continue
            visited[near] = 1

            sub_len, leaf = dfs(near, now_near)
            if sub_len > max_sub:
                max_sub = sub_len
                deepest_leaf = leaf

        return total + max_sub, deepest_leaf

    return dfs(root, 0)


root_a, a = search_length(1)
a_b, b = search_length(a)

print(a_b)
