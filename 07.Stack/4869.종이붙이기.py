import sys
sys.stdin = open('4869.txt')

def paper(x):
    if x == 10:
        return 1
    elif x == 20:
        return 3
    else:
        return paper(x-10) + 2 * paper(x-20)

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    total = paper(N)

    print(f'#{tc} {total}')





