def secondLevel(new_id, point):
    while point < len(new_id):
        if new_id[point] >= 'a' and new_id[point] <= 'z':
            point += 1
        elif new_id[point] >= '0' and new_id[point] <= '9':
            point += 1
        elif new_id[point] == '-' or new_id[point] == '_' or new_id[point] == '.':
            point += 1
        else:
            new_id.pop(point)

    return new_id
def RemoveLevel(new_id, left, right):
    while right < len(new_id):
        if new_id[left] == '.' and new_id[right] == '.':
            new_id.pop(right)
        else:
            left += 1
            right += 1

    if len(new_id) > 0:
        if new_id[0] == '.':
            new_id.pop(0)
    if len(new_id) > 0:
        last = len(new_id) - 1
        if new_id[last] == '.':
            new_id.pop(last)


    return new_id

def lastLevel(new_id):
    last = new_id[-1]

    while len(new_id) < 3:
        new_id.append(last)

    return new_id

def answerIs(new_id):
    ans = ""
    for el in new_id:
        ans += el

    return ans

def solution(new_id):
    new_id = new_id.lower() #1단계
    new_id = list(new_id)
    point = 0

    new_id = secondLevel(new_id, point)  # 2단계
    print(new_id)
    new_id = RemoveLevel(new_id, 0, 1) #RemoveLevel (3,4) 단계

    if len(new_id) == 0:
        new_id.append('a')

    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id.pop(len(new_id)-1)

    if len(new_id) <= 2:
        new_id = lastLevel(new_id)

    answer = ''
    answer = answerIs(new_id)
    print(answer)

    return answer

# solution("...!@BaT#*..y.abcdefghijklm")
# solution("z-+.^.")
# solution("=.=")
# solution("123_.def")
# solution("abcdefghijklmn.p")
solution("00000000")


