def is_sosu(num):
    if num <= 1:
        return False
    for div in range(2, int(num ** 0.5) + 1):
        if num % div == 0:
            return False
    return True


def solution(n, k): 
    # k진수로 변환
    N = n
    jinsu = ""
    while n >= 1:
        q, r = n // k, n % k
        jinsu = str(r) + jinsu
        n = q
    
    # 소수 개수 구하기
    answer = 0
    snum = ""
    for i in range(len(jinsu)):
        s = jinsu[i]
        if s == "0":
            if snum and is_sosu(int(snum)):
                answer += 1
            snum = ""
        else:
            snum += s
            
    if snum and is_sosu(int(snum)):
        answer += 1
        
    return answer