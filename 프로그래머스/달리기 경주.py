def solution(players, callings):
    answer = []

    hashmap = {}

    for i, v in enumerate(players):
        hashmap[v] = i

    for el in callings:
        pre, post = hashmap[el] - 1, hashmap[el]
        hashmap[players[pre]] = post
        hashmap[players[post]] = pre

        players[pre], players[post] = players[post], players[pre]

    return players


# enumerate를 통해 인덱스와 value 값을 가져올 수 있음
