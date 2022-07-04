# #더하는것은 별로 상관없고
# #빼는거에 상관이 있다.
#
# expression = input()
#
# expression = list(expression)
# answer = []
# sign = []
# flag = 0
# tmp = ""
# for i in range(len(expression)):
#     if expression[i] != "+" and expression[i] != "-":
#         tmp += expression[i]
#         if i == len(expression) - 1:
#             answer.append(int(tmp))
#     else:
#         answer.append(int(tmp))
#         answer.append(expression[i])
#         tmp = ""
#
# idx = 1
# left = idx-1
# right = idx + 1
# while True:
#     if '+' not in answer:
#         break
#     if answer[idx] == '+':
#         answer[left] += answer[right]
#         answer.pop(idx)
#         answer.pop(idx)
#     else:
#         idx += 2
#         if idx > len(answer):
#             idx = 1
#         left = idx -1
#         right = idx + 1
#
#
# if len(answer) == 1:
#     print(answer[0])
# else:
#     left = 0
#     right = 2
#     ans = answer[0]
#     while right < len(answer):
#         ans -= answer[right]
#         right += 2
#     print(ans)



####### 두번째 풀이방법 #######
expression = input().split('-')
answer = []
sum = 0
for el in expression:
    tmp = el.split('+')
    for num in tmp:
        sum += int(num)
    answer.append(sum)
    sum = 0

idx = 1
while idx < len(answer):
    answer[0] -= answer[idx]
    idx += 1
print(answer[0])
