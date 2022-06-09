# 0 0 0 0 0
# 0 0 1 0 3
# 0 2 5 0 1
# 4 2 4 4 2
# 3 5 1 3 1
def solution(board, moves):
    stack = []
    answer = 0
    depth = len(board)
    for col in moves:
        for i in range(depth):
            if board[i][col-1] != 0:
                if(len(stack) > 0 and stack[-1] == board[i][col-1]):
                    stack.pop()
                    answer += 1
                else:
                    stack.append(board[i][col-1])
                board[i][col - 1] = 0
                break

    return answer

res = solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4])
print(res)

