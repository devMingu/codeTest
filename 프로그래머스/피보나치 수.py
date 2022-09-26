def fib(n):
    fibList=[0, 1, 1]
    if n==1 or n==2:
        return 1
    for i in range(3,n+1):
        fibList.append( fibList[i-1] + fibList[i-2] )
    print(fibList)
    return fibList

def solution(n):
    a = fibonachi(n)
    if n <= 2:
        answer = a
    else:
        answer = a[n]

    return answer


def fibonachi(n):
    fb = [0,1,1]

    start = 1
    end = 2


    if n <= 2:
        return 1

    for i in range(3, n+1):
        x = fb[start] + fb[end]
        fb.append(x)
        start += 1
        end += 1
    return fb

solution()

