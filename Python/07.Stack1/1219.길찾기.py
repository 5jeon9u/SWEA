import sys
sys.stdin = open('1219.txt')

def DFS(x):
    visited[x] = 1
    if x == 99: # 현재 방문한 정점번호가 도착지
        return 1

    for w in G[x]: # 방문한 정점번호가 도착지가 아니라면 해당 번화와 연결된 곳을 탐색해야함
        if not visited[w]: # 현재 방문하지 않은 정점 번호가 있다면
            if DFS(w): # 탐색
                return 1

    return 0

for i in range(1, 11):
    tc, num = map(int, input().split())  # 정점수, 간선수
    G = [[] for _ in range(100)]  # 유향 그래프

    lst = list(map(int, input().split()))

    for j in range(0, len(lst), 2):
        G[lst[j]].append(lst[j+1])

    visited = [0] * 100

    print(f'#{tc} {DFS(0)}')

