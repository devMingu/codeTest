def play(title):
    for i in range(4):
        if name[i] in title:
            idx = title.index(name[i])
            title = title[idx + 1::]
        else:
            return "I hate UCPC"
    return "I love UCPC"

title = input()

name = ["U", "C", "P", "C"]
ans = play(title)
print(ans)
# # 1. U

# idx = title.index("U")
# title = title[idx+1::]
# # 2. C
# idx = title.index("C")
# title = title[idx+1::]
# # 3. P
# idx = title.index("P")
# title = title[idx+1::]
# # 4. C
# idx = title.index("C")
# title = title[idx+1::]
#


# a = "abc"
# if("a" in a):
#     print("GOOD")