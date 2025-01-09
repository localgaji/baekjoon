def solution(topping):
    answer = 0
    
    set_left = set()
    set_right = set()
    mem = [0] * len(topping)
    
    for i in range(len(topping)):
        t = topping[i]
        set_left.add(t)
        mem[i] = len(set_left)
    
    for i in range(len(topping) - 1, 0, -1):
        t = topping[i]
        set_right.add(t)
        if len(set_right) == mem[i - 1]:
            answer += 1
            
    return answer