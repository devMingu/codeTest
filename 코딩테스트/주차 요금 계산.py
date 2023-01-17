def computeTime(time):
    tmp = time.split(':')
    hours = int(tmp[0])
    minuts = int(tmp[1])

    return (hours * 60 + minuts)


def makeCarsObj(records):
    cars = {}

    for el in records:
        print(el)
        element = el.split(' ')
        time = computeTime(element[0])
        carNumber = element[1]
        status = element[2]

        if carNumber not in cars:
            cars[carNumber] = [status, element[0]]
        # else:
        #     # 차량이 들어와있는 상태
        #     if cars[carNumber][0] == "IN":
        #         cars[carNumber][1] = time - cars[carNumber][1]
        #         cars[carNumber][0] = "OUT"
        #     # 차량이 나간 상태
        #     else:
        #         cars[carNumber][1] += time
        #         cars[carNumber][0] = 1

    return cars


def solution(fees, records):
    answer = []

    cars = makeCarsObj(records)
    print(cars)

fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
solution(fees, records)
