n = int(input())
arr = []
for _ in range(n):
    a, b = map(int, input().split())
    arr.append([a,b])


arr.sort()


#날짜가 겹치는 애들은
for i in range(n):
    