# N, L = map(int, input().split())
# leak_pos = list(map(int, input().split()))
#
# leak_pos.sort()
#
# last = leak_pos[-1]
#
# # 물이 새는 위치
# pos = [0 for _ in range(last + 1)]
# max_pos = [0 for _ in range(last + 1)]
# max_list = [[] for _ in range(N+1)]
#
# # 물이 새는 구간의 리스트가 만들어짐.
# for el in leak_pos:
#     pos[el] = 1
#
# L -= 1
#
# # 물이 새는 각 위치에서 최대로 줄일 수 있는 수를 구해보자.
# for el in leak_pos:
#     start = el - L//2 if el - L//2 >= 1 else 1
#     end = el + L//2 if el + L//2 <= last else last
#     max_cnt = pos[start: end + 1].count(1)
#     max_pos[el] = max_cnt
#
#     max_list[max_cnt].append(el)
#     # print('물이 새는 위치', el, '는 최대', pos[start: end + 1].count(1), '개를 막을 수 있습니다')
#
# answer = 0
# # 최대값을 찾아서 지운다음 pos에 반영해야함.
# for i in range(N, 0, -1):
#     while max_list[i]:
#         delete_pos = max_list[i].pop()
#         if pos[delete_pos]:
#             answer += 1
#             start = delete_pos - L//2 if delete_pos - L//2 >= 1 else 1
#             end = delete_pos + L//2 if delete_pos + L//2 <= last else last
#             for j in range(start, end + 1):
#                 if pos[j]:
#                     pos[j] = 0
#
# print(answer)


N, L = map(int, input().split())
leak_pos = list(map(int, input().split()))
leak_pos.sort()
cover = leak_pos[0] + L - 1
answer = 0
for i in range(1, N):
    if cover < leak_pos[i]:
        answer += 1
        cover = leak_pos[i] + L - 1

answer += 1
print(answer)