def solution(numbers):
    answer = ''
    tmp = list(map(str, numbers))

    # 최대 1000이하이기 때문에 3자리로 만족시켜주기 위해 3번 반복(한 자리 숫자를 세 자리 숫자로 바꾸기 위함)
    tmp.sort(key=lambda x:x*3 , reverse=True)
    print(tmp)

    for el in tmp:
        answer += el

    answer = int(answer)
    answer = str(answer)

    return answer

# solution([6, 10, 2])
# solution([3, 30, 34, 5, 9])

# 문자형 숫자를 사전순으로 정렬할 수 있다. '1111111111' < '3' 관계를 만족한다. 숫자와 다르게 생각!!!
