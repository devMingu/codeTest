def solution(n, plans, clients):
    answer = []
    plan = []
    dic = {}
    for el in plans:
        plan.append(el.split(' '))
    #key는 부가서비스 value는 요금제
    for i in range(1, n+1):
        flag = 0
        idx = 0
        dic[i] = []
        for el in plan:
            if str(i) in el:
                dic[i].append(idx+1)
                flag = 1
                idx += 1
                continue
            if flag == 1:
                dic[i].append(idx+1)
                idx += 1
            else:
                idx += 1
    for el in clients:
        temp = el.split(' ')
        want_plan = temp[1::]
        right = 1
        listed = dic[int(want_plan[0])]
        while right < len(want_plan):
            listed = set(listed) & set(dic[int(want_plan[right])])
            listed = list(listed)
            right += 1

        check = 0
        if len(listed) != 0:
            for choose in listed:
                # print(temp[0], plan[choose-1][0])
                if int(temp[0]) <= int(plan[choose-1][0]):
                    answer.append(choose)
                    check = 1
                    break
            if check == 0:
                answer.append(0)
        else:
            answer.append(0)

    return answer

print(solution(4, ["38 2 3", "394 1 4"], ["10 2 3", "300 1 2 3 4", "500 1"]))

