from collections import deque

def solution(maps):
    R, C = len(maps), len(maps[0])
    INF = R * C + 1

    dr, dc = (0, 0, -1, 1), (1, -1, 0, 0)
    distance = [[INF] * C for _ in range(R)]
    distance[0][0] = 1
    q = deque([(0, 0)])

    while q:
        r, c = q.popleft()
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            
            if not (0 <= nr < R and 0 <= nc < C):
                continue
            if not maps[nr][nc]:
                continue
            if distance[nr][nc] <= distance[r][c] + 1:
                continue
            
            distance[nr][nc] = distance[r][c] + 1
            
            if (nr, nc) == (R-1, C-1):
                return distance[nr][nc]
            
            q.append((nr, nc))
            
    return -1