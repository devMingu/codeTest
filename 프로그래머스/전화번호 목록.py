# def solution(phone_book):
#     n = len(phone_book)
#     phone_book.sort()
#
#     left = 0
#     right = left + 1
#     while right < n:
#         k = len(phone_book[left])
#         if phone_book[left] == phone_book[right][:k]:
#             return False
#         left += 1
#         right += 1
#
#
#     return True
# #
# #
# a = solution(["119", "97674223", "1195524421"])
# b = solution(["123","456","789"])
# c = solution(["12","123","1235","567","88"])
#
# print(a,b,c)

def solution(phone_book):
    h = {}

    for number in phone_book:
        h[number] = 1

    for number in phone_book:
        temp = ""
        for el in number:
            temp += el
            if temp in h and temp != number:
                return False

    return True

a = solution(["119", "97674223", "1195524421"])
b = solution(["123","456","789"])
c = solution(["12","123","1235","567","88"])
print(a,b,c)