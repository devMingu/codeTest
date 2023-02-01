N = int(input())
M = int(input())
position = list(map(int, input().split()))

prev = position[0]
heights = position[0]

for i in range(1, len(position)):
    current = position[i]
    tmp = abs(prev - current)

    if tmp % 2 == 0:
        tmp //= 2
    else:
        tmp = tmp//2 + 1

    heights = max(heights, tmp)
    prev = current

last = abs(position[-1] - N)
heights = max(heights, last)

print(heights)
