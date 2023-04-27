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
