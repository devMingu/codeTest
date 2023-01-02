import sys
input = sys.stdin.readline
def findChocolateSize(K):
    c = 1
    while c < K:
        c *= 2
    return c

def findDivideCount(K, chocoSize):
    answer = K
    cnt = 0
    while answer:
        if answer >= chocoSize:
            answer -= (chocoSize)
        else:
            cnt += 1
            chocoSize //= 2
    return cnt

K = int(input())
chocoSize = findChocolateSize(K)
count = findDivideCount(K, chocoSize)

print(chocoSize, count)
