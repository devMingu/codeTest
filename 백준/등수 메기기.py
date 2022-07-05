import sys
input = sys.stdin.readline

n = int(input())
score = []

for i in range(n):
    score.append(int(input()))

score.sort()

start = 0
last = n-1
answer = 0
while start <= last:
    answer += abs(score[start] - (start+1)) + abs(score[last] - (last+1))
    if start == last:
        answer -= abs(score[start] - (start+1))
    start += 1
    last -= 1

print(answer)







