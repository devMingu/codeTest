def solution(board, moves):
    stack = []
    answer = 0
    depth = len(board)
    for col in moves:
        for i in range(depth):
            if board[i][col-1] != 0:
                # print(board[i][col-1], "입니다")
                if(len(stack) > 0 and stack[-1] == board[i][col-1]):
                    stack.pop()
                    answer += 2
                else:
                    stack.append(board[i][col-1])
                board[i][col - 1] = 0
                break

    return answer