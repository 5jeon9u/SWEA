import sys
sys.stdin = open('5203.txt')

def baby(num1, num2):
    if first[num1] >= 3:
        return 1
    else:
        for k in range(8):
            if first[k] >= 1 and first[k+1] >= 1 and first[k+2] >= 1:
                return 1

    if second[num2] >= 3:
        return 2

    else:
        for k in range(8):
            if second[k] >= 1 and second[k+1] >= 1 and second[k+2] >= 1:
                return 2
    return 0

T = int(input())
for tc in range(1, T+1):
    lst = list(map(int, input().split()))
    first = [0] * 10
    second = [0] * 10
    ans = 0

    for i in range(0, 12, 2):
        a = lst[i]
        b = lst[i+1]
        first[a] += 1
        second[b] += 1
        ans = baby(a, b)
        if ans == 1 or ans == 2:
            break
    print(f'#{tc} {ans}')




