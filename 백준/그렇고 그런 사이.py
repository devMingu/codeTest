N, K = map(int, input().split())

original = [i for i in range(1, N+1)]
answer = [0] * N
idx = 0
for i in range(N-1, 0, -1):
    if K >= i:
        K -= i
        original[i] = -1
        answer[idx] = i+1
        idx += 1

for i in range(N):
    if original[i] != -1:
        answer[idx] = original[i]
        idx += 1

for el in answer:
    print(el, end = ' ')






# for (int i=n-1; i>0; i--) {
#         if (k >= i) {
#             k -= i;
#             original[i] = -1;
#             changed[changed_num++] = i+1;
#         }
#     }

# 1 2 3 4 5
#
# 5 1 2 3 4
#
# 5 4 1 2 3
#



