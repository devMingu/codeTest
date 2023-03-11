def reverse_el(el):
    if el == 0:
        return 1
    return 0

def press_zero_idx():
    current[0] = reverse_el(current[0])
    current[1] = reverse_el(current[1])

    prev = 0
    next = 1
    count = 1
    while next < len(current):
        if current[prev] != toBe[prev]:
            # next 버튼을 눌러야함.
            count += 1
            current[next-1] = reverse_el(current[next-1])
            current[next] = reverse_el(current[next])
            if next < len(current) - 1:
                current[next+1] = reverse_el(current[next+1])
        prev += 1
        next += 1

    if current == toBe:
        return count
    else:
        return -1




def not_press_zero_idx():
    prev = 0
    next = 1
    count = 0
    while next < len(tmp):
        if tmp[prev] != toBe[prev]:
            # next 버튼을 눌러야함.
            count += 1
            tmp[next-1] = reverse_el(tmp[next-1])
            tmp[next] = reverse_el(tmp[next])
            if next < len(tmp) - 1:
                tmp[next+1] = reverse_el(tmp[next+1])
        prev += 1
        next += 1


    if tmp == toBe:
        return count
    else:
        return -1


n = int(input())

current = list(map(int, input()))
toBe = list(map(int, input()))
tmp = []

for el in current:
    tmp.append(el)

ans1 = press_zero_idx()
ans2 = not_press_zero_idx()

# print(ans1, ans2)

if ans1 == -1 and ans2 == -1:
    print(-1)

elif ans1 == -1 or ans2 == -1:
    print(ans2 + ans1 + 1)

else:
    print(min(ans1, ans2))

