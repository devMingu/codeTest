def solution(name):
    array = ['A'] * len(name)
    name = list(name)
    cnt = 0
    #현재의 위치에서 왼쪽으로 이동하는 경우 vs 오른쪽으로 이동하는 경우를 고려
    #만약 문자열에 name에 'a'가 없다면 그냥 순서대로 이동하면 됨.
    start = 0
    point = 0
    check = 0
    end = start + 1
    flag = 1
    while array != name:
        el = name[start]
        if el == 'A':
            if check == 0:
                point = start
            check = 1
            if name[start+1] == 'A':

            else:
                go_forward = abs((check - 1) - (start + 1))
                go_backward =
        else:
            array[start] = el
            cnt += min(ord(el) - ord('A'), ord('Z') - ord(el) + 1)
            start += 1
            cnt += 1
            end += 1



    cnt -= 1
    print(cnt)
    answer = 0
    return answer

solution('JEROEN')