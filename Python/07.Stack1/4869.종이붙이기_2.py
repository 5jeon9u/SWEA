import sys
sys.stdin = open('4869.txt')
N = 4 # 길이
arr = []
cnt = 0
def paper(n): # 현재 종이의 길이
    if n > N : # 종이의 길이가 범위를 넘어갈 때
        return
    if n == N:
        global cnt
        cnt += 1
        print(n, *arr)
    else:
        # 선택의 트리를 구성
        arr.append('I')
        paper(n + 1)
        arr.pop()

        arr.append('ㅁ')
        paper(n + 2)
        arr.pop()

        arr.append('=')
        paper(n + 2)
        arr.pop()

paper(0)
print('cnt = ', cnt)




