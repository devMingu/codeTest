def solution(brown, yellow):
    answer = []
    n = brown + yellow

    for x in range(n, 0, -1):
        if (n % x) == 0:
            y = n // x
            if x >= y:  # (x, y)쌍
                tmp = (x * 2) + ((y - 2) * 2)
                if tmp == brown:
                    break
    answer.append([x, y])
    return answer[0]





# def solution(brown, yellow):
#     answer = []
#     n = brown + yellow
#     x = n
#     while True:
#         if (n%x) == 0:
#             y = n // x
#             if x >= y: #(x, y)쌍
#                 tmp = (x * 2) + ((y-2) * 2)
#                 if tmp == brown:
#                     break
#         x -= 1
#     answer.append([x,y])
#     return answer[0]



