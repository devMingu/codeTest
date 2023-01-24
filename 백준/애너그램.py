def isAnagram(a, b):
    a_list = list(a)
    b_list = list(b)

    result = ""
    for el in b_list:
        if el in a_list:
            idx = a_list.index(el)
            result += a_list.pop(idx)
    if result == b:
        return True
    return False

n = int(input())

while n:
    a, b = input().split(' ')
    if isAnagram(a, b) and len(a) == len(b):
        print("%s & %s are anagrams." %(a, b))
    else:
        print("%s & %s are NOT anagrams." %(a, b))
    n -= 1


