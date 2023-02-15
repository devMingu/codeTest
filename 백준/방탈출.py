# n = int(input())
#
# memo = list(map(int, input().split()))
# lights = [0]*n
#
# idx = 0
# answer = 0
#
# for el in memo:
#     if lights[idx] == el:
#         idx += 1
#         continue
#     else:
#         tmp = idx
#         answer += 1
#         while tmp < n and tmp < idx + 3:
#             if lights[tmp] == 0:
#                 lights[tmp] = 1
#             else:
#                 lights[tmp] = 0
#             tmp += 1
#     idx += 1
#
# print(answer)










