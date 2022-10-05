def solution(arr):
    answer = 1
    n = len(arr)
    for i in range(n):
        tmp = list(str(arr[i]))
        tmp.sort()
        arr[i] = tmp
    arr.sort()

    left = 0
    right = 1
    while len(arr) > 1:
        if arr[left] == arr[right]:
            tmp = arr.pop(right)

        else:
            answer += 1
            tmp = arr.pop(left)
    return answer

# 자릿수가 틀리면 절대 같을 수 없다.

solution([112, 1814, 121, 1481, 1184]) #2
solution([123,456,789,321,654,987]) #3
solution([1,2,3,1,2,3,4]) #4
solution([123,234,213,432,234,1234,2341,12345,324]) #4


#애너그램 문제. 위치를 바꿔서 동일한 숫자들의 그룹의 개수 찾기.
