def match_count(numbers: list, set_numbers: set):
    count = 0
    for e in numbers:
        if e in set_numbers:
            count += 1
    return count


def generate_combinations(max_num):
    combins: list[set[int]] = []

    def dfs(com, start):
        if len(com) == 5:
            combins.append(set(com))
            return
        for num in range(start, max_num + 1):
            com.append(num)
            dfs(com, num + 1)
            com.pop()

    dfs([], 1)
    
    return combins


def solution(max_num, questions, ans):
    M = len(questions)
    combins = generate_combinations(max_num)
    
    C = len(combins)
    survive = [1] * C

    for m in range(M):
        quest, answer = questions[m], ans[m]
        for c in range(C):
            if not survive[c]:
                continue
            match = match_count(quest, combins[c])
            if match != answer:
                survive[c] = 0

    return survive.count(1)