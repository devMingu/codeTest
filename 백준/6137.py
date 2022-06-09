

n = int(input())
arr = []

for _ in range(n):
    arr.append(input())

left = 0
right = len(arr)-1
answer = ""
while left <= right:
    if arr[left] > arr[right]:
        answer += arr[right]
        right -= 1
    elif arr[left] < arr[right]:
        answer += arr[left]
        left += 1
    else:
        temp_left = left+1
        temp_right = right-1
        flag = 0
        while temp_left <= temp_right:
            if arr[temp_left] < arr[temp_right]:
                flag = 1
                break
            elif arr[temp_left] > arr[temp_right]:
                flag = 2
                break
            temp_left += 1
            temp_right -= 1
        if flag == 1:
            answer += arr[left]
            left += 1
        elif flag == 2:
            answer += arr[right]
            right -= 1
        else:   #전부 같을때
            answer += arr[left]
            left += 1

answer = list(answer)
cnt = 0
for el in answer:
    print(el, end='')
    cnt += 1
    if cnt % 80 == 0:
        print()

