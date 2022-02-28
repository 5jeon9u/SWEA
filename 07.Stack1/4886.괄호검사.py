import sys
sys.stdin = open('4886.txt')

T = int(input())

for tc in range(1, T+1):
    lst = list(map(str, input()))

    stack = []
    top = -1

    for i in range(len(lst)):
        if lst[i] == '(' or lst[i] == '{':
            stack.append(lst[i])
            top += 1

        elif lst[i] == ')':
            if top < 0: # 값이 남아있어야 꺼낼 수 있음
                result = 0
            else:
                val = stack.pop()
                top -= 1
                if val == '(':
                    result = 1
                else:
                    result = 0
                    break

        elif lst[i] == '}':
            if top < 0:  # 값이 남아있어야 꺼낼 수 있음
                result = 0
            else:
                val = stack.pop()
                top -= 1
                if val == '{':
                    result = 1
                else:
                    result = 0
                    break

    if top > -1: # 스택에 남아 있는 것이 있으면 안됨
        result = 0

    print(f'#{tc} {result}')