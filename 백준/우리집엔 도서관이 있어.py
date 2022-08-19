# 1. 알파벳 순으로 정렬
# 2. 사전 순으로 가장 앞서는 책을 위에, 뒤에 있는 책은 밑에
# 3. 책을 정렬하는 방법은 책하나를 빼서 위에 올려놓는법.

import sys
input = sys.stdin.readline

n = int(input())
books = []
for _ in range(n):
    books.append(int(input()))
left = 0
right = left + 1


answer = []
cnt = 0
for i in range(n-1, -1, -1):
    #움직이지 않아도 되는 책들을 구해서( 전체에서 빼준다 )
    if books[i] == n:
        cnt += 1
        n -= 1

print(len(books)-cnt)




