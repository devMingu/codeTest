alp = {
    'A': 3,
    'B': 2,
    'C': 1,
    'D': 2,
    'E': 3,
    'F': 3,
    'G': 2,
    'H': 3,
    'I': 3,
    'J': 2,
    'K': 2,
    'L': 1,
    'M': 2,
    'N': 2,
    'O': 1,
    'P': 2,
    'Q': 2,
    'R': 2,
    'S': 1,
    'T': 2,
    'U': 1,
    'V': 1,
    'W': 1,
    'X': 2,
    'Y': 2,
    'Z': 1
}

a = input()
b = input()

a = list(a)
b = list(b)
n = len(a)

tmp1 = []
tmp2 = []
for i in range(n):
    tmp1.append(alp[a[i]])
    tmp1.append(alp[b[i]])


while len(tmp1) > 2:
    left = 0
    right = 1
    while right < len(tmp1):
        tmp2.append((tmp1[left] + tmp1[right])%10)
        left += 1
        right += 1

    tmp1.clear()
    tmp1 = tmp2.copy()
    tmp2 = []


x1 = str(tmp1[0])
x2 = str(tmp1[1])
answer = x1 + x2
print(answer)


