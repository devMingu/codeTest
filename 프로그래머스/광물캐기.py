from collections import deque


def make_picks_list(picks):
    pick_list = deque([])

    p = ["diamond", "iron", "stone"]
    idx = 0
    for rang in picks:
        for i in range(rang):
            pick_list.append(p[idx])

        idx += 1

    return pick_list


def cal_sum(array):
    mine = {
        "diamond": 25,
        "iron": 5,
        "stone": 1,
    }
    total_sum = 0
    for el in array:
        total_sum += mine[el]

    return total_sum


def find_answer(selected_pick, mines):
    res = 0
    for el in mines:
        # 곡괭이가 다이아일때
        if selected_pick == "diamond":
            res += 1

        # 곡괭이가 철일때
        elif selected_pick == "iron":
            if el == "diamond":
                res += 5
            else:
                res += 1

        # 곡괭이가 돌일때
        else:
            if el == "diamond":
                res += 25
            elif el == "iron":
                res += 5
            else:
                res += 1

    print(selected_pick, res)
    return res


def solution(picks, minerals):
    answer = 0

    picks_list = make_picks_list(picks)

    # 곡괭이가 얼마나 필요한가?
    n = len(minerals) // 5
    if len(minerals) % 5 != 0:
        n += 1

    # 그렇지 않다면, 가장 피로도가 많이 들어가는곳에 다이아 > 철 > 돌 순으로 사용해야함.
    total_pickk = picks[0] + picks[1] + picks[2]

    tmp_list = []
    for i in range(0, len(minerals), 5):
        if (i + 5) > len(minerals):
            end = len(minerals)
        else:
            end = i + 5
        tmp = minerals[i:end]
        total = cal_sum(tmp)
        tmp_list.append([total, tmp])
        total_pickk -= 1

        if total_pickk <= 0:
            break

    tmp_list.sort(key=lambda x: -x[0])

    # 곡괭이를 선택해서 캐면 됌. 곡괭이 선택을 HOW?
    for el in tmp_list:
        if picks_list:
            selected_pic = picks_list.popleft()
            answer += find_answer(selected_pic, el[1])
        else:
            break

    return answer