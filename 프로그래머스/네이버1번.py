# def solution(n, arr1, arr2):
#     r1 = []
#     r2 = []
#
#     for i in range(n):
#         r1.append(to_Binary(arr1[i], n))
#         r2.append(to_Binary(arr2[i], n))
#
#     answer = []
#     return answer
#
#
# def to_Binary(number, n):
#     binary = [0] * n
#     idx = n - 1
#     while number > 0:
#         binary[idx] = number % 2
#         idx -= 1
#         number //= 2
#     return binary
#
#
# solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28])


a = 1
b = 1

if a == b == 1:
    print("GGOD")