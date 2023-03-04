def make_sequence_of_keyboard(keymap):
    keyboard = {}

    for key_pos in keymap:
        pos = 1
        for el in key_pos:
            if el not in keyboard:
                keyboard[el] = pos
            else:
                prev_pos = keyboard[el]
                if prev_pos > pos:
                    keyboard[el] = pos
            pos += 1
    return keyboard

def count_key(targets, keyboard):
    result = []
    for el in targets:
        ans = 0
        for item in el:
           if item in keyboard:
               ans += keyboard[item]
           else:
               ans = -1
               break

        result.append(ans)

    return result

def solution(keymap, targets):
    # answer = []
    keyboard = make_sequence_of_keyboard(keymap)
    # print(keyboard)
    answer = count_key(targets, keyboard)


    print(answer)
    return answer



######## 두 번째 풀이방법 ##########

# def solution(keymap, targets): # 두 번째 풀이법
#     answer = []
#
#     for item in targets:
#         res = 0
#         for el in item:
#             min_pos = 101
#             flag = 0
#             for keyItem in keymap:
#                 if el in keyItem:
#                     min_pos = min(keyItem.index(el) + 1, min_pos)
#                     flag = 1
#
#             if flag == 0:
#                 res = -1
#                 break
#             res += min_pos
#         answer.append(res)
#
#     print(answer)
#     return answer


solution(["ABACD", "BCEFD"], ["ABCD","AABB"])
solution(["AA"], ["B"])
solution(["AGZ", "BSSS"], ["ASA","BGZ"])
solution(["ABACD", "BCEFD"], ["XABCD", "AABB"])
solution(["AA"], ["BA", "C"])
solution(["0"], ["0"])