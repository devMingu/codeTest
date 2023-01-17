import math


def computeTime(time):
    tmp = time.split(':')
    hours = int(tmp[0])
    minuts = int(tmp[1])

    return (hours * 60 + minuts)


def makeCarsObj(records):
    cars = {}
    for record in records:

        element = record.split(' ')
        time = computeTime(element[0])
        carNumber = element[1]
        status = element[2]

        if carNumber not in cars:
            cars[carNumber] = [status, -time]
        else:
            # 차량이 들어와있는 상태
            if cars[carNumber][0] == "IN":
                cars[carNumber][1] += time
                cars[carNumber][0] = "OUT"
            # 차량이 나간 상태
            else:
                cars[carNumber][1] -= time
                cars[carNumber][0] = "IN"
    cars = isAllOfCarsOut(cars)
    return cars


def isAllOfCarsOut(cars):
    lastTime = computeTime("23:59")
    for key, values in cars.items():
        if values[0] == "IN":
            values[0] = "OUT"
            values[1] += lastTime

    return cars


def computePrice(fees, cars):
    result = []

    normalTime = fees[0]
    normalPrice = fees[1]
    chargeTime = fees[2]
    price = fees[3]

    for key, values in cars.items():
        if values[1] <= normalTime:
            result.append([key, normalPrice])
            continue

        tmp = normalPrice + math.ceil((values[1] - normalTime) / chargeTime) * price
        result.append([key, tmp])

    result.sort()
    return result


def solution(fees, records):
    answer = []

    cars = makeCarsObj(records)

    result = computePrice(fees, cars)

    for el in result:
        answer.append(el[1])

    return answer