# 연속된 수열의 길이가 3이상이 아니라면 2 출력
# 1. 연속해서 커지는 경우
# 2. 연속해서 작아지는 경우

# 4 1 3 3 2 2 9 2 3

# 1 5 3 6 4 7 1 3 2 9 5

n = int(input())
k = list(map(int, input().split()))


left = 0
right = 1
cnt = 1

answer = 0
while right < n:
    if k[left] <= k[right]:
        cnt += 1
    else:
        answer = max(answer, cnt)
        cnt = 1
    left += 1
    right += 1

if cnt != 1:
    answer = max(answer, cnt)
    cnt = 1

left = 0
right = 1
while right < n:
    if k[left] >= k[right]:
        cnt += 1
    else:
        answer = max(answer, cnt)
        cnt = 1
    left += 1
    right += 1

if cnt != 1:
    answer = max(answer, cnt)

if n == 1:
    answer = 1
print(answer)


