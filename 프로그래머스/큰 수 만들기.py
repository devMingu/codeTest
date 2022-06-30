def solution(number, k):
    number = list(number)
    answer = ''
    start = 0
    end = len(number) - k + 1
    k_copy = k
    for i in range(k, 0, -1):
        tmp = max(number[start:end])
        print(number, end)
        answer += str(tmp)
        number = number[number.index(tmp)+1::]
        end = len(number) - k_copy + 2
        k_copy -= 1


    print(answer)



    return answer

solution("1231234", 3)
