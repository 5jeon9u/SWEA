import sys
sys.stdin = open('1225.txt')

for tc in range(1, 11):
    N = int(input())
    pwd = list(map(int, input().split()))
    QSIZE = len(pwd)

    front = -1
    rear = len(pwd) -1

    while pwd[-1] > 0:
        for i in range(1, 6):
            update_pwd = pwd.pop(0) - i
            pwd.append(update_pwd)

            if pwd[-1] <= 0:
                pwd[-1] = 0
                break

    print(f'#{tc}', *pwd)
