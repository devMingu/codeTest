def solution(periods, payments, estimates):
    vip_cnt = 0
    vip_not_cnt = 0
    idx = 0
    answer = []
    for period in periods:
        if period>=23:
            if period >= 59:
                if period == 59:
                    if sum(payments[idx]) >= 900000:
                        if sum(payments[idx]) - payments[idx][0] + estimates[idx] < 600000:
                            vip_not_cnt += 1
                    else:
                        if sum(payments[idx]) - payments[idx][0] + estimates[idx] >= 600000:
                            vip_cnt += 1
                else:
                    if sum(payments[idx]) >= 600000:
                        if sum(payments[idx]) - payments[idx][0] + estimates[idx] < 600000:
                            vip_not_cnt += 1
                    else:
                        if sum(payments[idx]) - payments[idx][0] + estimates[idx] >= 600000:
                            vip_cnt += 1
            else:
                if period == 23:
                    if sum(payments[idx]) - payments[idx][0] + estimates[idx] >= 900000:
                        vip_cnt += 1
                else:
                    if sum(payments[idx]) >= 900000:    #이번달은 vip
                        if sum(payments[idx]) - payments[idx][0] + estimates[idx] < 900000:
                            vip_not_cnt += 1
                        #유지 not?
                    else: #vip가 아닌 고객
                        if sum(payments[idx]) - payments[idx][0] + estimates[idx] >= 900000:
                            vip_cnt += 1
        idx += 1
    answer.append(vip_cnt)
    answer.append(vip_not_cnt)
    return answer

print(solution([20, 23, 24],
               [
                [100000, 100000, 100000, 100000, 100000, 100000, 100000,100000,100000,100000,100000,100000],
                [100000, 100000, 100000, 100000, 100000, 100000, 100000,100000,100000,100000,100000,100000],
                [350000, 50000, 50000, 50000, 50000, 50000, 50000,50000,50000,50000,50000,50000]
               ],
               [100000,100000,100000]))

#
# [100000, 100000, 100000, 100000, 100000, 100000, 100000,100000,100000,100000,100000,100000]
# [350000, 50000, 50000, 50000, 50000, 50000, 50000,50000,50000,50000,50000,50000]
