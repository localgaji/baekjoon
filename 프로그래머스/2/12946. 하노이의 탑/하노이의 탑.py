def solution(N):
    answer = []

    def move(a, b):
        answer.append([a, b])
    
    def recursive(n, dep, arr):
        if n == 0:
            return
        stop = 6 - dep - arr
        recursive(n - 1, dep, stop)
        move(dep, arr)
        recursive(n - 1, stop, arr)
        
    recursive(N, 1, 3)
        
    return answer