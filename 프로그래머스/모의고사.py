def solution(numbers):
    n = len(numbers)
    i = 1
    answer = []
    for el in numbers:
        for j in range(i, n):
            answer.append(el + numbers[j])
        i += 1
    answer = set(answer)
    answer = list(answer)
    answer.sort()
    return answer

solution([2,1,3,4,1])