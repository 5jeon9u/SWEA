import sys
sys.stdin = open('5188.txt')

def move(x, y, z):
    global ans
    if x == (N-1) and y == (N-1):
        if ans > z:
            ans = z
    elif y+1 > N-1:
        move(x+1, y, z+arr[x+1][y])
    elif x+1 > N-1:
        move(x, y+1, z+arr[x][y+1])
    else:
        move(x, y+1, z+arr[x][y+1])
        move(x+1, y, z+arr[x+1][y])


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0Xfffffff
    move(0, 0, arr[0][0])
    print(f'#{tc} {ans}')