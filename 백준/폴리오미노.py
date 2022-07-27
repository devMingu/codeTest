# 1. X가 홀 수 일때 -1
# 2. .에 대하여 나누어 생각해볼 수 있다.

element = input()
element = list(element)

box = []
tmp = ''
x_flag = 0
dot_flag = 0
for el in element:
    if el == 'X':
        if dot_flag == 1:
            box.append(tmp)
            tmp = ''
            dot_flag = 0
        x_flag = 1
    else:
        if x_flag == 1:
            box.append(tmp)
            tmp = ''
            x_flag = 0

        dot_flag = 1
    tmp += el
box.append(tmp)

a = 'AAAA'
b = 'BB'
answer = ''

for el in box:
    if el.__contains__('.'):
        answer += el
        continue
    X_length = len(el)
    if X_length % 2 == 0:
        a_cnt = X_length // 4
        b_cnt = (X_length % 4) // 2
        for i in range(a_cnt):
            answer += a
        for i in range(b_cnt):
            answer += b

    else:
        answer = '-1'
        break


print(answer)


