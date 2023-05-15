def is_available(el):
    available = ["aya", "ye", "woo", "ma"]
    el_list = list(el)

    result = ""
    prev = ""
    ans = ""

    for alp in el_list:
        result += alp
        if result in available:
            if prev != result:
                ans += result

            prev = result
            result = ""

    if el == ans:
        return 1
    return 0


def solution(babbling):
    answer = 0

    for el in babbling:
        answer += is_available(el)

    return answer