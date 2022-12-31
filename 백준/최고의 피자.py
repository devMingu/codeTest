# #열량이 가장 높은 피자.
#
# dough = []
# n = int(input())
# a, b = map(int, input().split()) #도우 가격 ,토핑 가격
# c = int(input())    #도우의 열량
#
# for i in range(n):
#     dough.append(int(input()))
# dough.sort(reverse=True)
#
# #토핑을 하나도 넣지 않았을때 1원당 열량.
# answer = c//a
#
# idx = 0
# cnt = 1
# sum_calorie = dough[0]
# while idx < n:
#     tmp = (c + sum_calorie) // (a + b*cnt)
#     if answer <= tmp:
#         answer = tmp
#     else:
#         break
#     idx += 1
#     cnt += 1
#     if idx < n:
#         sum_calorie += dough[idx]
#
#
# print(answer)









