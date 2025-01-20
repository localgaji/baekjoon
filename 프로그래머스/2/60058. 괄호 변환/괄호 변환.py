def fix_u(u):
    new_u = ""    
    for s in u[1:-1]:
        if s == "(":
            new_u += ")"
        else:
            new_u += "("
    return new_u


def is_right(w):
    stack = []
    for s in w:
        if s == ")" and stack and stack[-1] == "(":
            stack.pop()
        else:
            stack.append(s)
    if stack:
        return False
    return True


def separate(w):
    u, v = "", ""
    count_1, count_2 = 0, 0
    for i in range(len(w)):
        s = w[i]
        if s == "(":
            count_1 += 1
        else:
            count_2 += 1
            
        if i >= 1 and count_1 == count_2:
            u = w[0: i + 1]
            if i + 1 < len(w):
                v = w[i + 1:]
            break
            
    return u, v


def recursive(w):
    if w == "":
        return w
    u, v = separate(w)
    if is_right(u):
        new_v = recursive(v)
        return u + new_v

    return "(" + recursive(v) + ")" + fix_u(u)
    
    
def solution(p):
    return recursive(p)