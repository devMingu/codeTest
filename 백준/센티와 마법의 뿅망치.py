import heapq
import sys
input = sys.stdin.readline
N, H, T = map(int, input().split())

answer = 0
h = []
for _ in range(N):
    t = int(input())
    heapq.heappush(h, -t)

while -h[0] > 1 and -h[0] >= H and T:
    max_titan = heapq.heappop(h)
    heapq.heappush(h, max_titan/2)
    answer += 1
    T -= 1

if -h[0] >= H:
    print("NO")
    print(int(-h[0]))
else:
    print("YES")
    print(answer)


