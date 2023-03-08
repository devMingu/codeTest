def solution(food):
    answer = ''
    left = ''
    for i in range(1, len(food)):
        count = food[i]
        wei = count // 2

        left += str(i) * wei

    answer += left
    answer += "0"
    answer += left[::-1]

    return answer