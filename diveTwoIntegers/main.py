def solution(numbers, hand):
    arr = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        ['*', 0, '#']
    ]
    left = [3,0]
    right = [3,2]
    answer = ''
    for el in numbers:
        #왼손
        if el == 1 or el == 4 or el == 7:
            if el == 1:
                left = [0,0]
                answer += "L"
            elif el ==  4:
                left = [1,0]
                answer += "L"
            else:
                left = [2,0]
                answer += "L"
        #오른손
        elif el == 3 or el == 6 or el == 9:
            if el == 3:
                right = [0,2]
                answer += "R"
            elif el == 6:
                right = [1,2]
                answer += "R"
            else:
                right = [2,2]
                answer += "R"
        else:
            if el == 2:
                left_len = abs(left[0]-0) + abs(left[1] - 1)
                right_len = abs(right[0]-0) + abs(right[1] - 1)
                if left_len == right_len:
                    if hand=="left":
                        left = [0,1]
                        answer += "L"
                    else:
                        right = [0,1]
                        answer += "R"
                elif left_len < right_len:
                    left = [0,1]
                    answer += "L"
                else:
                    right = [0,1]
                    answer += "R"
            elif el == 5:
                left_len = abs(left[0] - 1) + abs(left[1] - 1)
                right_len = abs(right[0] - 1) + abs(right[1] - 1)
                if left_len == right_len:
                    if hand=="left":
                        left = [1,1]
                        answer += "L"
                    else:
                        right = [1,1]
                        answer += "R"
                elif left_len < right_len:
                    left = [1,1]
                    answer += "L"
                else:
                    right = [1,1]
                    answer += "R"
            elif el == 8:
                left_len = abs(left[0] - 2) + abs(left[1] - 1)
                right_len = abs(right[0] - 2) + abs(right[1] - 1)
                if left_len == right_len:
                    if hand=="left":
                        left = [2,1]
                        answer += "L"
                    else:
                        right = [2,1]
                        answer += "R"
                elif left_len < right_len:
                    left = [2,1]
                    answer += "L"
                else:
                    right = [2,1]
                    answer += "R"
            else:
                left_len = abs(left[0] - 3) + abs(left[1] - 1)
                right_len = abs(right[0] - 3) + abs(right[1] - 1)
                if left_len == right_len:
                    if hand=="left":
                        left = [3,1]
                        answer += "L"
                    else:
                        right = [3,1]
                        answer += "R"
                elif left_len < right_len:
                    left = [3,1]
                    answer += "L"
                else:
                    right = [3,1]
                    answer += "R"

    return answer


res = solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right")
print(res)
