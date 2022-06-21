def solution(record):
    answer = []
    user = {}
    for msg in record:
        str_split = msg.split(' ')
        if str_split[0] == 'Enter': #Enter
            user[str_split[1]] = str_split[2]
        elif str_split[0] == 'Change':   #chagne
            user[str_split[1]] = str_split[2]
        else:   #leave
            continue

    for msg in record:
        str_split = msg.split(' ')
        if str_split[0] == 'Enter': #Enter
            answer.append(user[str_split[1]] + '님이 들어왔습니다.')
        elif str_split[0] == 'Change':   #chagne
            continue
        else:   #leave
            answer.append(user[str_split[1]] + '님이 나갔습니다.')

    # print(answer)
    return answer


solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])

