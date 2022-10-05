# 'strawberry' 'carrot' 'watermelon' 'melon'

def show():
    total = 0
    discount = 0

    # total
    for key, values in market.items():
        total += market[key][0] * market[key][1]

    # discount
    for key, values in market.items():
        cnt = market[key][0]
        if key == 'strawberry':
            if cnt < 10:
                price = 300
            elif cnt < 20:
                price = 270
            else:
                price = 220

        elif key == 'carrot':
            if cnt < 10:
                price = 500
            elif cnt < 20:
                price = 450
            else:
                price = 370

        elif key == 'watermelon':
            if cnt < 3:
                price = 2000
            else:
                price = 1600
        else: #melon
            if cnt < 5:
                price = 1000
            else:
                price = 800
        discount += (cnt * price)


    print('Here is recipt. Total price is', str(total)+".", 'Discount price is', str(discount) + ".")


def currentState():
    a = market["strawberry"][0]
    b = market["carrot"][0]
    c = market["watermelon"][0]
    d = market["melon"][0]

    print("strawberry :", str(a) +"," , "carrot :" , str(b) +"," , "watermelon :" , str(c) + "," , "melon :" , str(d))






market = {
    "strawberry" : [0, 300],
    "carrot" : [0, 500],
    "watermelon" : [0, 2000],
    "melon" : [0, 1000]
}



while True:
    initial_input = int(input('0 : calculate, 1 : add\n'))

    if initial_input == 0:
        show()
        break
    else:
        product = input()

        if product not in market:
            print("no product in market")
        else:
            num = int(input())
            market[product][0] += num

        currentState()




