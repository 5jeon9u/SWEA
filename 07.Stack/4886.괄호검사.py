# 괄호 체크
# 괄호 사이에는 포함 관계만 존재한다 = {()}
# 여는 괄호 순서의 역순으로 닫는 괄호 순서로 나와야함 -> 이거 체크하려고 개념적으로 stack 사용
# 여는 괄호만 스택에 나오는 순서를 저장하고, 닫는 괄호는 미저장
# 닫는 괄호가 나올 때마다 스택의 맨 마지막에 있는 거랑 비교
# 맞으면 스택에서 지우는 식으로 반복
# 찾을때 있어야 하고 , 끝나고 남아잇으면 안됨
# pop 할때는 비어있는지 여부를 항상 확인해야함

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