def solution(R, C, queries):
    answer = []
    matrix = [[C * r + (c + 1) for c in range(C)] for r in range(R)]

    for q in queries:
        r1, c1, r2, c2 = q[0] - 1, q[1] - 1, q[2] - 1, q[3] - 1
        prev = matrix[r1 + 1][c1]
        compare = R * C + 1

        # 위
        for c in range(c1, c2):
            now = matrix[r1][c]
            matrix[r1][c] = prev
            prev = now
            compare = min(compare, now)
        # 오
        for r in range(r1, r2):
            now = matrix[r][c2]
            matrix[r][c2] = prev
            prev = now
            compare = min(compare, now)

        # 아래
        for c in range(c2, c1, -1):
            now = matrix[r2][c]
            matrix[r2][c] = prev
            prev = now
            compare = min(compare, now)

        # 왼
        for r in range(r2, r1, -1):
            now = matrix[r][c1]
            matrix[r][c1] = prev
            prev = now
            compare = min(compare, now)

        answer.append(compare)

    return answer
