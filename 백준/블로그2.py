n = int(input())
blog = list(input())

#RED로 가득 채웠을때.
r_cnt = 1
b_cnt = 1
start = 0
end = 1
#전부 파란색으로 칠할때.
while end < n:
    if blog[start] == 'R':
        b_cnt += 1
        if blog[end] == 'R' and end < n-1:
            b_cnt -= 1
    else:
        if end == n-1 and blog[end] == 'R':
            b_cnt += 1

    start += 1
    end += 1

#전부 빨간색으로 칠할때.
start = 0
end = 1
while end < n:
    if blog[start] == 'B':
        r_cnt += 1
        if blog[end] == 'B' and end < n-1:
            r_cnt -= 1
    else:
        if end == n-1 and blog[end] == 'B':
            r_cnt += 1
    start += 1
    end += 1

print(min(r_cnt, b_cnt))





