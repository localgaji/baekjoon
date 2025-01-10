from collections import deque

def solution(dirs):
    drdc = {"U": (-1, 0), "D": (1, 0), "R": (0, 1), "L": (0, -1)}
    visited = set()
    
    r, c = 5, 5
    
    for d in dirs:
        dr, dc = drdc[d]
        nr, nc = r + dr, c + dc
        if not (0 <= nr <= 10 and 0 <= nc <= 10):
            continue
        
        forward = (r, c, nr, nc)
        reverse = (nr, nc, r, c)
        
        if forward not in visited and reverse not in visited:
            visited.add(forward)
            
        r, c = nr, nc
        
    return len(visited)