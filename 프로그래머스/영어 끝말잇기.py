def isOverlap(words, end_idx, value):
    if value in words[:end_idx]:
        return False
    return True


def isCotinuous(words, prev, current):
    # print("isContinuous", words[prev], words[current])
    if words[prev][-1] == words[current][0]:
        return True
    return False


def solution(n, words):
    answer = [0, 0]

    members = {}
    idx = 0
    words_idx = 0
    my_turn = 1
    while words_idx < len(words):
        value = words[words_idx]
        if not isOverlap(words, words_idx, value):
            return [words_idx % n + 1, words_idx // n + 1]
        if not isCotinuous(words, words_idx - 1, words_idx) and words_idx > 0:
            return [words_idx % n + 1, words_idx // n + 1]

        words_idx += 1

    return answer