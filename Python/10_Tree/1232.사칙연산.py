import sys
sys.stdin = open('1232.txt')

def postorder(v):
    cal = ['+', '-', '*', '/']
    global stack

    if v == 0:
        return
    postorder(L[v])
    postorder(R[v])

    if P[v] in cal:
        b = stack.pop()
        a = stack.pop()
        if P[v] == '+':
            stack.append(a+b)
        elif P[v] == '-':
            stack.append(a-b)
        elif P[v] == '/':
            stack.append(a//b)
        elif P[v] == '*':
            stack.append(a*b)
    else:
        stack.append(int(P[v]))

for tc in range(1, 11):
    N = int(input())

    stack = []

    L = [0] * (N + 1)
    R = [0] * (N + 1)
    P = [0] * (N + 1)

    for i in range(1, N+1):
        arr = list(input().split())
        tmp = [0] * 4

        for j in range(len(arr)):
            tmp[j] = arr[j]

        P[i] = tmp[1]
        L[i] = int(tmp[2])
        R[i] = int(tmp[3])

    postorder(1)
    print(f'#{tc} {stack[0]}')
