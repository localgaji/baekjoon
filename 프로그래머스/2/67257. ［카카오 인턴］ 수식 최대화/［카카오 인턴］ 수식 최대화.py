def aob(a, b, o):
    if o == "+":
        return a + b
    if o == "-":
        return a - b
    return a * b
    

def operate(o, arr):
    stack = []
    for num in arr:
        if stack and stack[-1] == o:
            stack.pop()
            a = stack.pop()
            b = num
            stack.append(aob(a,b,o))
        else:
            stack.append(num)
    return stack


def make_orders():
    orders = []
    
    
    def dfs(order):
        if len(order) == 3:
            orders.append(order)
            return 
        
        for o in ["+", "-", "*"]:
            if o in order:
                continue
            dfs(order + [o])
    
    
    dfs([])
    
    return orders


def solution(expression):
    
    arr = []
    orders = make_orders()
    
    num = ""
    for e in expression:
        if e in "0123456789":
            num += e
        else:
            if num:
                arr.append(int(num))
            arr.append(e)
            num = ""
    arr.append(int(num))
    
    compare = 0
    for order in orders:
        stack = arr[:]
        for o in order:
            stack = operate(o, stack)
        result = stack[0]
        if result < 0:
            result = -1 * result
        if result > compare:
            compare = result
        
    return compare