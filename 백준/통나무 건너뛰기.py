t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(int(x) for x in input().split())
    arr.sort()
    answer = ""
    answer += str(arr[-1])
    #N이 홀수일때 -> 떨어짐
    right = n-2
    left = right-1
    while left >= 0:
        answer = str(arr[left]) + " " +answer + " " + str(arr[right])
        left -= 2
        right -= 2
    #N이 짝수일때 -> 하나가 남는다.
    if n % 2 == 0:
        answer = str(arr[0]) + " " + answer

    itrable = answer.split(' ')
    maxL = abs(int(itrable[0]) - int(itrable[-1]))
    start = 0
    end = 1
    while end < n:
        temp = abs(int(itrable[start]) - int(itrable[end]))
        maxL = max(temp, maxL)
        start += 1
        end += 1
    print(maxL)





