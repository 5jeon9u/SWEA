import sys
sys.stdin = open('4874.txt')

T = int(input())

oper = ['+', '-', '*', '/', '.']

for tc in range(1, T+1):
    lst = list(map(str, input().split()))
    stack = []
    top = -1
    result = 0
    for i in lst:
        if i in oper:
            if i == '.':
                result = stack.pop()
                top -= 1
                break
            else:
                if top < 1: # 피연산자가 2개 미만으로 남아있는 경우
                    result = 'error'
                    break
                b = int(stack.pop())
                a = int(stack.pop())
                if i == '+':
                    stack.append(a+b)
                elif i == '-':
                    stack.append(a-b)
                elif i == '*':
                    stack.append(a*b)
                elif i == '/':
                    stack.append(int(a/b))
                top -= 1
        else:
            stack.append(i)
            top += 1

    if top > -1: # 스택에 값이 남아있는 경우
        result = 'error'
        print(f'#{tc} {result}')
    else:
        print(f'#{tc} {result}')





