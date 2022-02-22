import sys
sys.stdin = open('12398.txt')

T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split()) # 노드 수 : V, 간선 수 : E
    lst = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split()) # 출발 노드 : S, 도착 노드 : G

    stack = []

    for i in range(E):
        if lst[i][0] == S:
            stack.append(lst[i][1])

