
case = int(input())


while case > 0:
    arr = []
    cnt = 0
    n, m = map(int, input().split())
    for _ in range(m):
        a, b = map(int, input().split())
        arr.append([a,b])
    arr = sorted(arr, key=lambda x:x[1])

    books = [1]*(n+1)

    for a, b in arr:
        for i in range(a, b+1):
            if books[i] == 1:
                cnt += 1
                books[i] = 0
                break
    print(cnt)
    case -= 1







