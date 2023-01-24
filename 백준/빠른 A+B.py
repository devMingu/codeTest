import sys
input = sys.stdin.readline

n = int(input())

while n:
    a, b = map(int, input().split())
    print(a + b)
    n -= 1