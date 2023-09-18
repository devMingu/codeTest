N = int(input())
load_length = list(map(int, input().split()))
oil_price = list(map(int, input().split()))

position = 0
current_oil_price = oil_price[position]
answer = current_oil_price * load_length[position]

for i in range(1, len(load_length)):
    if current_oil_price > oil_price[i]:
        current_oil_price = oil_price[i]

    answer += current_oil_price * load_length[i]

print(answer)

