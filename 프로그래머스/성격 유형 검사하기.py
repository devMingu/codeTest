# 코드 리팩토링

def survey_score(choice):
    return choice - 4 if choice >= 4 else 4 - choice


def solution(survey, choices):
    answer = ''
    type_index = ["RT", "CF", "JM", "AN"]
    idx = 0
    char_type = {}

    for el in survey:
        disagree_el, agree_el = el[0], el[1]
        choice = choices[idx]

        score = survey_score(choice)
        if choice >= 5:
            char_type[agree_el] = score if agree_el not in char_type else char_type[agree_el] + score
        else:
            char_type[disagree_el] = score if disagree_el not in char_type else char_type[disagree_el] + score

        idx += 1

    for el in type_index:
        t1 = char_type[el[0]] if el[0] in char_type else 0
        t2 = char_type[el[1]] if el[1] in char_type else 0

        answer += el[0] if t1 >= t2 else el[1]

    return answer







# def survey_score(choice):
#     if choice >= 5:
#         if choice == 5:
#             return 1
#         elif choice == 6:
#             return 2
#         else:
#             return 3
#     if choice <= 3:
#         if choice == 1:
#             return 3
#         elif choice == 2:
#             return 2
#         else:
#             return 1
#
#     return 0
#
#
# def solution(survey, choices):
#     answer = ''
#
#     idx = 0
#
#     char_type = {}
#     for el in survey:
#         disagree_el = el[0]
#         agree_el = el[1]
#         choice = choices[idx]
#
#         idx += 1
#
#         score = survey_score(choice)
#         if choice >= 5:
#             if agree_el not in char_type:
#                 char_type[agree_el] = score
#             else:
#                 char_type[agree_el] += score
#         if choice <= 3:
#             if disagree_el not in char_type:
#                 char_type[disagree_el] = score
#             else:
#                 char_type[disagree_el] += score
#
#     print(char_type)
#
#     type_index = ["RT", "CF", "JM", "AN"]
#     for el in type_index:
#         t1 = char_type[el[0]] if el[0] in char_type else 0
#         t2 = char_type[el[1]] if el[1] in char_type else 0
#
#         answer += el[0] if t1 >= t2 else el[1]
#
#     return answer