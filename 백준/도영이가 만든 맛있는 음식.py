from itertools import combinations

def combi(idxItems, k):
    return list(combinations(idxItems, k))

def calculateSB(idxCombi, food):
    answer = 1_000_000_000
    for el in idxCombi:
        s_tmp = 1
        b_tmp = 0
        for idx in el:
            s_tmp *= food[idx][0]
            b_tmp += food[idx][1]

        tmp = abs(s_tmp - b_tmp)

        if answer > tmp:
            answer = tmp
    return answer

n = int(input())

food = []
idxItems = [i for i in range(n)]
answer = 1_000_000_000
for _ in range(n):
    s, b = map(int, input().split())
    food.append([s,b])


for i in range(1, n+1):
    idxCombi = combi(idxItems, i)
    ans = calculateSB(idxCombi, food)
    if ans == 0:
        answer = 0
        break
    if answer > ans:
        answer = ans

print(answer)

# 가능한 모든 조합을 찾아야겠다.
# 조합
# if 신맛과 쓴맛의 차이가 0이라면 종료.
