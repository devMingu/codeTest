import sys
input = sys.stdin.readline


N = int(input())
height = list(map(int, input().split()))

answer = 0
now = 0
next = 1

tmp_cnt = 0
while next < N:
    if height[now] > height[next]:
        tmp_cnt += 1
        next += 1
    else:
        answer = answer if answer > tmp_cnt else tmp_cnt
        tmp_cnt = 0
        now = next
        next += 1
answer = answer if answer > tmp_cnt else tmp_cnt
print(answer)


