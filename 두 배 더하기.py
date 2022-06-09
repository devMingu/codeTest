# 값을 하나 증가  -> 홀수는 짝수, 짝수는 홀수
# 모든 값을 두배 증가 -> 짝수

#모든 값을 두배 증가시키는것은 하나라도 값에 도달하면 쓰지 못한다.

n = int(input())
arr = list(int(x) for x in input().split())
arr.sort()

cnt = 0

while sum(arr) != 0:
    check = 0
    for i in range(n):
        if arr[i] % 2 != 0 or arr[i] == 0 or arr[i] == 1:
            if arr[i] == 0:
                continue
            else:
                arr[i] -=1
                cnt += 1
            check = 1
    if check == 0:
        for i in range(n):
            arr[i] //= 2
        cnt += 1

print(cnt)
