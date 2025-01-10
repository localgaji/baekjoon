def solution(word):
    #dictionary = {"A": 1, "E": 2, "I": 3, "O": 4, "U": 5}
    #target = []
    answer = [0]
    count = [0]
    
    def dfs(cur):
        count[0] += 1
        
        if cur == word:
            answer[0] = count[0]
            
        if len(cur) == 5 or answer[0] > 0:
            return 
        
        for i in range(5):
            char = "AEIOU"[i]
            dfs(cur + char)
    
    dfs("")
    
    return answer[0] - 1