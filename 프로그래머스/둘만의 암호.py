def remove_alp(alp, skip):
    skip = list(skip)
    skip.sort(reverse=True)

    while skip:
        delete_item = skip.pop()
        alp.pop(alp.index(delete_item))

    return alp


def solution(s, skip, index):
    answer = ''
    alp = ["a", "b", "c", "d", "e", "f", "g",
           "h", "i", "j", "k", "l", "m", "n", "o", "p",
           "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    alp = remove_alp(alp, skip)
    n = len(alp)

    for el in list(s):
        idx = (alp.index(el) + index) % n

        answer += alp[idx]

    return answer