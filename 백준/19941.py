n, k = map(int, input().split())
position = list(input())

left = 0
right = n
cnt = 0
for i in range(n):
    left = i-k
    right = i+1+k
    if i-k < 0:
        left = 0
    if i+k > n:
        right = n
    if position[i] == 'P':
        if 'H' in position[left:right]:
            idx = position[left:right].index('H') + left
            position[idx] = 'Z'
            cnt += 1
print(cnt)


