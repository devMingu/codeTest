# from collections import deque
#
# def solution(people, limit):
#     deq = deque(sorted(people))
#     answer = 0
#     #50 50 70 80
#     while len(deq) > 1:
#         x = deq[0] + deq[-1]
#         if x > limit:
#             deq.pop()
#         else:
#             deq.popleft()
#             deq.pop()
#         answer += 1
#     if len(deq) == 1:
#         answer += 1
#     return answer
#
#
#
# print(solution([70,50,80], 100))
# # binary_seacrh([70,50,80,50], 50)

a = [5,4,3]
a.sort(reverse=)