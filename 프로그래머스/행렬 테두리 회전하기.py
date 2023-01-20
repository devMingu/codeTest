import heapq


def transform_matrix(x1, y1, x2, y2, matrix, rows, columns):
    tmp = []
    min_list = []
    for i in range(y2 - 1, y1 - 1, -1):
        matrix[x1][i], matrix[x1][i + 1] = matrix[x1][i + 1], matrix[x1][i]
        heapq.heappush(min_list, matrix[x1][i + 1])
        heapq.heappush(min_list, matrix[x1][i])
    for i in range(x1, x2):
        matrix[i][y1], matrix[i + 1][y1] = matrix[i + 1][y1], matrix[i][y1]
        heapq.heappush(min_list, matrix[i + 1][y1])
        heapq.heappush(min_list, matrix[i][y1])
    for i in range(y1, y2):
        matrix[x2][i], matrix[x2][i + 1] = matrix[x2][i + 1], matrix[x2][i]
        heapq.heappush(min_list, matrix[x2][i + 1])
        heapq.heappush(min_list, matrix[x2][i])
    for i in range(x2 - 1, x1, -1):
        matrix[i][y2], matrix[i + 1][y2] = matrix[i + 1][y2], matrix[i][y2]
        heapq.heappush(min_list, matrix[i + 1][y2])
        heapq.heappush(min_list, matrix[i][y2])
    return [matrix, heapq.heappop(min_list)]


def create_matrix(rows, columns):
    idx = 1
    matrix = []
    for i in range(rows):
        tmp = []
        for j in range(columns):
            tmp.append(idx)
            idx += 1
        matrix.append(tmp)

    return matrix


def solution(rows, columns, queries):
    matrix = create_matrix(rows, columns)
    answer = []
    for el in queries:
        x1 = el[0] - 1
        y1 = el[1] - 1
        x2 = el[2] - 1
        y2 = el[3] - 1
        result = transform_matrix(x1, y1, x2, y2, matrix, rows, columns)
        matrix = result[0]
        answer.append(result[1])

    return answer