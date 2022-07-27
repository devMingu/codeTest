# 1. 학교를 기준으로 좌/ 우를 나눈다.
# 2. 가장 멀리있는 집부터 방문.

N, K, S = map(int, input().split()) #N 아파트 단지, K 통학버스 정원 S 학교 위치.
apart = [0]*100000
start = 1000001
end = -1
for i in range(N):
    location, student = map(int, input().split())
    start = min(start, location)
    end = max(end, location)
    apart[location] = student


# 7 4 4
# 0 5
# 1 2
# 2 3
# 6 4
# 7 6
# 8 6
# 9 7
# start ~ K and K ~ end       0(5) 1(2) 2(3) *** 6(4) 7(6) 8(6) 9(7)  4*2 4*2 2*2        5*2 5*2 4*2 4*2 3*2 2*2
# 8 8 4 10 10 8 8 6 4

answer = 0
left_bus = 0
left = start
check_left = 0
while left < S:
    if left_bus < K:
        #tmp는 태울 수 있는 학생의 수 K - left_bus
        tmp = K - left_bus
        if tmp <= apart[left]:
            left_bus += tmp
        else:
            left_bus += apart[left]
        apart[left] -= tmp

        if apart[left] <= 0:
            left += 1
        else:
            answer += abs(S - start) * 2
            left_bus = 0
    else:
        check_left = 1
        answer += abs(S - start) * 2
        start = left
        left_bus = 0

if check_left == 0 and left < S:
    answer += abs(S-start) * 2

print(answer)
# 5(3) 7(3) 11(5) 20(4)
right = end
right_bus = 0
check_right = 0
while S < right:
    if right_bus < K:
        #tmp는 태울 수 있는 학생의 수 K - left_bus
        tmp = K - right_bus
        if tmp <= apart[right]:
            right_bus += tmp
        else:
            right_bus += apart[right]
        apart[right] -= tmp

        if apart[right] <= 0:
            right -= 1
        else:
            print(answer, end)
            answer += abs(S - end) * 2
            right_bus = 0
    else:
        check_right = 1
        print(answer, end, '!')
        answer += abs(S - end) * 2
        end = right
        right_bus = 0

if check_right == 0 and right > S:
    answer += abs(S-end) * 2

print(answer)









