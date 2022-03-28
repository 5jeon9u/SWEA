import sys
sys.stdin = open('1224.txt')

for tc in range(1, 11):
    N = int(input())
    cal = input()

    icp = {'+' : 1, '*' : 2, '(': 3, ')': 3}
    isp = {'+' : 1, '*' : 2, '(': 0 }

    stack = []
    new_cal = []

    for i in cal:
        if i in icp:
            if i == ')':
                while stack[-1] != '(':
                    new_cal.append(stack.pop())
                stack.pop()
            else:
                while stack and isp[stack[-1]] >= icp[i]:
                    new_cal.append(stack.pop())
                stack.append(i)
        else:
            new_cal.append(i)

    while stack: # 남아있는 연산자 출력
        new_cal.append(stack.pop())

    for j in new_cal:
        if j in icp:
            b = int(stack.pop())
            a = int(stack.pop())
            if j == '+':
                stack.append(a+b)
            else:
                stack.append(a*b)
        else:
            stack.append(j)

    print(f'#{tc} {stack[0]}')
