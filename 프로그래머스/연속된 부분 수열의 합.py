def solution(sequence, k):
    n = len(sequence)

    start = 0
    end = 0

    a_s = 0
    a_e = 0
    max_len = n
    i = 0

    while start < n and end < n:
        if i == 0:
            tmp = sequence[0]
            if tmp == k:
                if max_len > (end - start):
                    max_len = end - start
                    a_s = start
                    a_e = end
            end += 1
            if end >= n:
                break
            tmp += sequence[end]
            i += 1

        if tmp == k:
            if max_len > (end - start):
                max_len = end - start
                a_s = start
                a_e = end
            tmp -= sequence[start]
            start += 1
            end += 1
            if end >= n:
                break

            tmp += sequence[end]

        elif tmp > k:
            tmp -= sequence[start]
            start += 1

        else:
            end += 1
            if end >= n:
                break

            tmp += sequence[end]

    answer = [a_s, a_e]

    return answer