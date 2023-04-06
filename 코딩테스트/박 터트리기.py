def __main__():
    N, K = map(int, input().split())  # N개의 공, K 바구니
    minimum = K * (K + 1) // 2

    if minimum > N:
        return -1
    elif (N - minimum) % K == 0:
        return K - 1
    else:
        return K

answer = __main__()
print(answer)

# 수학적으로 생각해볼 줄 알아야함
