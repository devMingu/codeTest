# from collections import deque
#
#
# def solution(n, m, section):
#     answer = 0
#
#     section = deque(section)
#
#     while section:
#
#         start = section.popleft()
#         answer += 1
#         while section:
#             if section[0] >= start + m:
#                 break
#
#             section.popleft()
#
#     return answer
#
#
#
#
#


def make_wall_info(n, section):
    wall = [1 for _ in range(n+1)]
    for el in section:
        wall[el] = 0

    return wall

def make_paint(m):
    paint = [1 for _ in range(m)]
    return paint

def solution(n, m, section):
    answer = 0
    # result = [1 for _ in range(n+1)]

    wall = make_wall_info(n, section)
    paint = make_paint(m)

    for el in section:
        if wall[el] == 0:
            end = el + m if (el + m)  <= n+1 else n+1
            wall[el: end] = paint
            answer += 1

    return answer