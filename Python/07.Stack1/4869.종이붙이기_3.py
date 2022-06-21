import sys
sys.stdin = open('4869.txt')
N = 4 # 길이
cnt = 0
def paper(n): # 현재 종이의 길이
    if n > N : # 종이의 길이가 범위를 넘어갈 때
        return
    if n == N:
        global cnt
        cnt += 1
    else:
        # 선택의 트리를 구성
        paper(n + 1)
        paper(n + 2)
        paper(n + 2)

paper(0)
print('cnt = ', cnt)




