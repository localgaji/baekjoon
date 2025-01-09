def solution(numbers, target):
    answer = [0]

    def dfs(point, total):
        if point == len(numbers):
            if total == target:
                answer[0] += 1
            return

        number = numbers[point]
        dfs(point + 1, total + number)
        dfs(point + 1, total - number)

    dfs(0, 0)

    return answer[0]
