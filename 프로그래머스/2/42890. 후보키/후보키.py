from collections import deque


def is_unique(keys, relation):
    if not keys:
        return False

    visited = set()
    for row in relation:
        string = ""
        for col in keys:
            string += row[col]
            string += "_"

        if string in visited:
            return False

        visited.add(string)
    return True


def is_minimal(columns, keyset_list):
    column_set = set(columns)
    for keyset in keyset_list:
        all_in = True
        for key in keyset:
            if key not in column_set:
                all_in = False
                break
        if all_in:
            return False
    return True


def solution(relation):
    C = len(relation[0])
    keyset_list: list[set[int]] = []

    q: deque[[int]] = deque([[]])
    while q:
        keyset = q.popleft()

        if is_unique(keyset, relation) and is_minimal(keyset, keyset_list):
            keyset_list.append(set(keyset))
            continue

        if not keyset:
            start = 0
        else:
            start = keyset[-1] + 1
        for i in range(start, C):
            new_keyset = keyset + [i]
            q.append(new_keyset)

    return len(keyset_list)
