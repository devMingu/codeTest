B, C, D = map(int, input().split())

burgur = list(map(int, input().split()))
side_menu = list(map(int, input().split()))
beverage = list(map(int, input().split()))

burgur.sort(reverse=True)
side_menu.sort(reverse=True)
beverage.sort(reverse=True)

# 가능한 세트의 수는 각 메뉴가 가진 수의 최소
set_count = min(len(burgur), len(side_menu), len(beverage))


not_sale_sum = sum(burgur) + sum(side_menu) + sum(beverage)
answer = 0
for i in range(set_count):
    tmp = burgur.pop(0) + side_menu.pop(0) + beverage.pop(0)
    answer += (tmp * 0.9)

answer += sum(burgur) + sum(side_menu) + sum(beverage)

print(not_sale_sum)
print(int(answer))



