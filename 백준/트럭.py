from collections import deque

n, w, L = map(int, input().split())
truck_list = list(map(int, input().split()))
car_on_bridge = deque([])
time_on_bridge = []

idx = 0
next = 1
on_time = 1
car_on_bridge.append(truck_list.pop(0))
time_on_bridge.append(on_time)

while car_on_bridge:
    on_time += 1
    # 차량이 다리를 건넜는지
    if w + time_on_bridge[idx] == on_time:
        idx += 1
        car_on_bridge.popleft()

    # 다리위에 차량이 올라가도 되는지.
    if truck_list and (sum(car_on_bridge) + truck_list[0] <= L):
        car_on_bridge.append(truck_list.pop(0))
        time_on_bridge.append(on_time)

print(on_time)

# 들어온 시점 + 시간 > 다리길이





