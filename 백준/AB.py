# # 문자열의 길이 == N
# # 문자열은 A, B로 이루어져 있다
# # (i, j) == (A, B) 인 쌍이 K개 존재한다. (단, i < j)
#
# def countAB():
#     countAB = 0
#     for i in range(N):
#         if s[i] == 'A':
#             countAB += s[i+1::].count("B")
#         else:
#             continue
#     return countAB
# #
# #
# N, K = map(int, input().split())
# s = ['A' for _ in range(N)]
#
# flag = 0
# for i in range(N-1, -1, -1):
#     s[i] = 'B'
#     tmp = countAB()
#
#     if tmp < K:
#         continue
#     elif tmp == K:
#         flag = 1
#         break
#     else:
#         s[i] = 'A'
# if flag == 1:
#     for el in s:
#         print(el, end='')
# else:
#     print(-1)
#
#
#

