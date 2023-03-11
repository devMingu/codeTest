from collections import deque
def find_ten():
    tmp = []
    other = deque([])
    while cake:
        el = cake.popleft()
        if el % 10 == 0:
            tmp.append(el)
        else:
            other.append(el)
    tmp = find_other(other, tmp)
    return tmp

def find_other(other, tmp):
    while other:
        el = other.popleft()
        tmp.append(el)

    return tmp


N, M = map(int, input().split())
cake = list(map(int, input().split()))

cake.sort()
cake = deque(cake)

tmp_cake = deque(find_ten())
answer = []

while tmp_cake:
    if M < 1:
        break

    el = tmp_cake.popleft()

    if el == 10:
        answer.append(el)

    elif el > 10:
        tmp = el - 10
        answer.append(10)
        M -= 1
        if tmp > 10:
            tmp_cake.appendleft(tmp)
        elif tmp == 10:
            answer.append(10)


print(len(answer))