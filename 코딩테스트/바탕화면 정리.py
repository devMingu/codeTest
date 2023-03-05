def left(wallpaper):
    min_left = len(wallpaper[0])-1
    for el in wallpaper:
        if "#" in el:
            # print(el.index("#"))
            idx = el.index("#")
            min_left = min(idx, min_left)
    return min_left


def right(wallpaper):
    min_right = 0
    for el in wallpaper:
        if "#" in el:
            for i in range(len(el)-1, -1, -1):
                if el[i] == "#":
                    min_right = max(i, min_right)
                    break

    return min_right + 1

def height_min(wallpaper):
    idx = 0
    for el in wallpaper:
        if "#" in el:
            return idx
        idx += 1
    return idx
def height_max(wallpaper):
    idx = len(wallpaper)
    # max_idx = 0
    for j in range(len(wallpaper)-1, -1, -1):
        if "#" in wallpaper[j]:
            return j + 1

    return idx



def solution(wallpaper):
    # answer = []
    left_v = left(wallpaper)
    right_v = right(wallpaper)
    height_min_v = height_min(wallpaper)
    height_max_v = height_max(wallpaper)
    answer = [height_min_v, left_v, height_max_v, right_v]
    return answer



solution([".#...", "..#..", "...#."])
solution(["..........", ".....#....", "......##..", "...##.....", "....#....."])
solution([".##...##.", "#..#.#..#", "#...#...#", ".#.....#.", "..#...#..", "...#.#...", "....#...."])
solution(["..", "#."])
solution(["..", "#.", "#."])
