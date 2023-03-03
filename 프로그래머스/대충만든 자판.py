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
               return [-1]

        result.append(ans)

    return result

def solution(keymap, targets):
    # answer = []
    keyboard = make_sequence_of_keyboard(keymap)
    # print(keyboard)
    answer = count_key(targets, keyboard)


    print(answer)
    return answer

# solution(["ABACD", "BCEFD"], ["ABCD","AABB"])
# solution(["AA"], ["B"])
# solution(["AGZ", "BSSS"], ["ASA","BGZ"])
solution(["ABACD", "BCEFD"], ["XABCD", "AABB"])
solution(["AA"], ["BA"])
solution(["0"], ["0"])