def find(value):
    first = 0
    second = 1
    third = first + second
    while True:
        if third > value:
            return second
        else:
            first = second
            second = third
            third = first + second

N = int(input())

while N:
    value = int(input())
    answer = []
    while value:
        tmp = find(value)
        answer.append(tmp)
        value -= tmp
    answer.sort()
    for el in answer:
        print(el, end = ' ')
    print()

    N -= 1



