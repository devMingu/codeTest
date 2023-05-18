def find_max():
    s_list = list(s)
    tmp = ""
    answer = ""
    for el in s_list:
        if el == "K":
            n = len(tmp)
            answer += str(5*(10**n))
            tmp = ""
            continue
        tmp += el

    for i in range(len(tmp)):
        answer += "1"
    print(answer)

def find_min():
    s_list = list(s)
    tmp = ""
    answer = ""
    for el in s_list:
        if el == "K":
            n = len(tmp)
            if len(tmp):
                answer += str(10 ** (n - 1))
            answer += "5"
            tmp = ""
            continue
        tmp += el

    if len(tmp):
        answer += str(10**(len(tmp) - 1))
    print(answer)

s = input()
find_max()
find_min()