def solution(sequence, k):
    n = len(sequence)

    start = 0
    end = 1

    a_s = 0
    a_e = 0
    max_len = n

    tmp = sequence[start]

    while start < n:

        if tmp == k:
            if max_len > (end - start):
                max_len = end - start
                a_s = start
                a_e = end

            start += 1
            end += 1


        elif tmp < k:
            end += 1
            if end < n:
                tmp += sequence[end]
            else:
                end -= 1
                start += 1

        else:
            tmp -= sequence[start]
            start += 1

    answer = [a_s, a_e - 1]

    return answer