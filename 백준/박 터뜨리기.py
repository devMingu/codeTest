import sys
input = sys.stdin.readline

n = int(input())
teams = list(map(int, input().split()))
teams.sort()

# 1 2 3 5 7 9
idx_start = 0
idx_end = len(teams) - 1

while idx_start < idx_end:
    answer = teams[idx_start] + teams[idx_end]
    start = idx_start + 1
    end = idx_end - 1
    flag = 0
    while start < end:
        tmp = teams[start] + teams[end]

        if tmp < answer:
            flag = 1
            break
        else:
            start += 1
            end -= 1
    if flag == 0:
        print(answer)
        break
    else:
        flag = 0

    idx_start += 1
    idx_end -= 1








