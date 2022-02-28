import sys
sys.stdin = open('12398.txt')

T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())  # 정점수, 간선수
    G = [[] * (V+1)]
    S, G = map(int, input().split())


    print(G)
