def doubleOrOneThing(array):
    result = ""
    temp = ""
    for i in range(len(array) - 1):
        print(i)
        if array[i] < array[i + 1]:
            result += array[i] * 2
        elif array[i] > array[i+1]:
            result += array[i]
        else:
            temp = result
            for j in range(i, len(array)):
                temp += array[i]
                if array[i] < array[j]:
                    result = temp
                    temp = ""
                    i = j
                    break
                else:
                    result += array[j]
                    i = j






    result += array[-1]

    return result


n = int(input())

for i in range(n):
    t = input()
    res = doubleOrOneThing(t)
    print("Case #" + str(i + 1) + ": " + res)


