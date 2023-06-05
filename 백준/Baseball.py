T = int(input())

for _ in range(T):
    inning = 9
    yonsei_univ_score = 0
    korea_univ_score = 0

    while inning:
        score = list(map(int, input().split()))
        yonsei, korea = score[0], score[1]

        yonsei_univ_score += yonsei
        korea_univ_score += korea

        inning -= 1

    if yonsei_univ_score < korea_univ_score:
        print("Korea")
    elif yonsei_univ_score > korea_univ_score:
        print("Yonsei")
    else:
        print("Draw")