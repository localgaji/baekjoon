import heapq
import sys

input = sys.stdin.readline

D, B = map(int, input().split())
dias = [tuple(map(int, input().split())) for _ in range(D)]
bags = [int(input()) for _ in range(B)]

dias.sort(key=lambda x: x[0], reverse=True)
bags.sort()

pq = []
answer = 0
for b in bags:
    while dias and dias[-1][0] <= b:
        w, c = dias.pop()
        heapq.heappush(pq, (-c, w))
    if not pq:
        continue
    answer -= heapq.heappop(pq)[0]

print(answer)
