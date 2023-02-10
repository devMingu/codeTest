n = list(input())
answer = ""

stack = []

for el in n:
    stack.append(el)
    if stack[-4:] == ["P", "P", "A", "P"]:
        idx = 4
        while idx:
            stack.pop()
            idx -= 1
        stack.append("P")

if stack == ["P", "P", "A", "P"] or stack == ["P"]:
    print("PPAP")
else:
    print("NP")