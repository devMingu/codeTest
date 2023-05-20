N, L = map(int, input().split())

pos = 0
answer = 0
for _ in range(N):
    D, R, G = map(int, input().split())

    answer += (D - pos)
    pos = D

    if answer % (R+G) <= R:
        answer += R - (answer % (R+G))

answer += (L - pos)

print(answer)
