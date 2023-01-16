def makeNewArrayList():
    el.pop(maxIdx)
    tmp = []
    tmp.extend(el[:left])
    tmp.append(maxNum)
    tmp.extend(el[left::])

    return tmp

def findEndIdx():
    if left + S + 1 >= N:
        end = N
    else:
        end = left + S + 1

    return end

def isLeftEqual(left):
    if el[left] == maxNum:
        return True

    return False


N = int(input())
el = list(map(int, input().split()))
S = int(input())
left = 0
while S > 0 and left < N - 1:
    end = findEndIdx()

    maxNum = max(el[left: end])
    maxIdx = el.index(maxNum)

    if isLeftEqual(left):
        left += 1
        continue

    el = makeNewArrayList()
    S -= (maxIdx - left)
    left += 1

for num in el:
    print(num, end = ' ')