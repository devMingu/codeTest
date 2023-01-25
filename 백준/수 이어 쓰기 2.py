import sys
input = sys.stdin.readline
n, k = map(int, input().split())

digit = 1
num = 9
target = 0
while k > num * digit:
    k -= (num * digit)
    digit += 1
    target += num
    num *= 10

target = (target + 1) + (k-1) // digit

if target > n:
    print(-1)
else:
    idx = (k-1) % digit
    print(str(target)[idx])
