import sys

input = sys.stdin.readline
grid = [list(map(int, list(input().rstrip()))) for _ in range(9)]
N = 9


def is_invalid(r, c, x):
    if x in grid[r]:
        return True

    for r_ in range(9):
        if grid[r_][c] == x:
            return True

    r_left = r // 3 * 3
    c_left = c // 3 * 3
    for r_ in range(r_left, r_left + 3):
        for c_ in range(c_left, c_left + 3):
            if grid[r_][c_] == x:
                return True

    return False


candidates = [[set() for _ in range(N)] for _ in range(N)]
unknown = set()

for r in range(9):
    for c in range(9):
        if grid[r][c] == 0:
            unknown.add((r, c))
            candidates[r][c] = set([i for i in range(1, 1 + N)])

while unknown:
    update_count = 0
    for r, c in list(unknown):
        for i in list(candidates[r][c]):
            if is_invalid(r, c, i):
                candidates[r][c].remove(i)
        if len(candidates[r][c]) == 1:
            grid[r][c] = candidates[r][c].pop()
            unknown.remove((r, c))
            update_count += 1
            continue
    if update_count == 0:
        break


def dfs(start):
    if len(unknown_list) == start:
        for row in grid:
            string = ""
            for c in row:
                string += str(c)
            print(string)
        exit()
        return

    r, c = unknown_list[start]

    for i in candidates_lists[r][c]:
        if is_invalid(r, c, i):
            continue

        grid[r][c] = i
        dfs(start + 1)
        grid[r][c] = 0


candidates_lists = [[sorted(list(candidates[r][c])) for c in range(N)] for r in range(N)]
unknown_list = sorted(list(unknown), key=lambda x: (x[0], x[1]))
dfs(0)
