def solution(n, m):
    answer = 0
    num = 2

    if n == 3: # 약수의 개수가 3이라는 말은( 지수가 2인 친구들이 3개의 약수를 가질 수 있다는 의미.)
        num1 = 4
        while m:
            n_cnt = find_divisor(num1)
            if n_cnt == n:
                answer = num1
                m -= 1
            num += 1
            num1 = num**2   # 약수의 개수가 3일때를 구하는 방법은 1씩 증가하지 않고 제곱해서 진행할 수 있다.
        return answer
    else:
        while m:
            n_cnt = find_divisor(num)
            if n_cnt == n:
                answer = num
                m -= 1
            num += 1
        return answer

def find_divisor(number):
    cnt = 0
    for i in range(1, int(number**(0.5) + 1)):
        if (number % i == 0):
            cnt += 1
            if (i != number//i):
                cnt +=1

        if cnt > 4:
            return -1

    return cnt

print(solution(3,3000))

# 약수가 