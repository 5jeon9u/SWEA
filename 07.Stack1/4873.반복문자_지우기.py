import sys
sys.stdin = open('4873.txt')

T = int(input())

for tc in range(1, T + 1):
    lst = input()

    top = -1
    stack = []

    for i in range(len(lst)):
        # 빈 스택 확인
        if top < 0:
            stack.append(lst[i]) #
            top += 1
        else:
            val = stack.pop()
            top -= 1
            if val != lst[i]:
                stack.append(val)
                stack.append(lst[i])
                top += 2

    print(f'#{tc} {top+1}')