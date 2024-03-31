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

    def dfs(now, total):
        max_sub = 0
        deepest_leaf = now
        for near, now_near in graph[now]:
            if visited[near]:
                continue
            visited[near] = 1

            leaf, sub_len = dfs(near, now_near)
            if sub_len > max_sub:
                max_sub = sub_len
                deepest_leaf = leaf

        return deepest_leaf, total + max_sub

    return dfs(root, 0)


a, root_a = search_length(1)
b, a_b = search_length(a)

print(a_b)
