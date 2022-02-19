# 없다는 것은 길이이로 알 수 있다
import sys
sys.stdin = open('5356.txt')

T = int(input())

for tc in range(1, T + 1):
    arr = [list(input()) for _ in range(5)]
    sols = []
    for j in range(15):
        for i in range(5):
            if j < len(arr[i]):
                sols.append(arr[i][j]) # i와 j의 순서 유의
    print(f'#{tc} {"".join(sols)}')

