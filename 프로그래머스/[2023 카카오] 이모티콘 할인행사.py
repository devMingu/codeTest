from itertools import product


def solution(users, emoticons):
    answer = []
    discountRate = [10, 20, 30, 40]

    permu = list(product(discountRate, repeat=len(emoticons)))

    # print(permu)

    talkPlus = 0
    totalEmoticon = 0

    for el in permu:
        tmpTalkPlus = 0
        tmpPriceEmoticon = 0
        for user in users:
            buy = 0
            idx = 0
            for per in el:
                if user[0] <= per:
                    # print(per, emoticons[idx], emoticons[idx]*(100-per)//100)
                    buy += emoticons[idx] * (100 - per) // 100
                idx += 1

            if buy >= user[1]:
                tmpTalkPlus += 1
            else:
                tmpPriceEmoticon += buy

        if talkPlus == tmpTalkPlus:
            if totalEmoticon < tmpPriceEmoticon:
                totalEmoticon = tmpPriceEmoticon

        elif talkPlus < tmpTalkPlus:
            talkPlus = tmpTalkPlus
            totalEmoticon = tmpPriceEmoticon

    answer.append(talkPlus)
    answer.append(totalEmoticon)

    return answer