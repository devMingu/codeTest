def make_list(list_array):
    tmp_list = [0 for _ in range(10)]
    set_tmp = set(list_array)
    set_tmp = list(set_tmp)
    for el in set_tmp:
        cnt = list_array.count(el)
        el = int(el)
        tmp_list[el] = cnt

    return tmp_list


def solution(X, Y):
    answer = ''

    X = list(X)
    Y = list(Y)

    X_list = make_list(X)
    Y_list = make_list(Y)

    for i in range(9, -1, -1):
        min_cnt = min(X_list[i], Y_list[i])
        if min_cnt != 0:
            answer += str(i) * min_cnt

    if len(answer) == 0:
        answer = "-1"

    if answer[0] == "0":
        answer = "0"
    return answer
