import sys
sys.stdin = open('5249.txt')

def find_set(x):
    if x != p[x]:
        p[x] = find_set(p[x])
    return p[x]

T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    edges = [] # 간선 리스트
    p = [i for i in range(V+1)]
    ans = 0  # 가중치를 더할 변수
    cnt = 0 # 노드의 수를 확인할 변수

    for _ in range(E):
        edges.append(tuple(map(int, input().split())))

    # 가중치들의 오름차순 정렬
    edges.sort(key=lambda x:x[2])
    
    # V-1개의 간선을 선택
    # 단, 사이클이 존재하면 안됨

    for edge in edges:
        u, v, w = edge
        # 연결 상태를 확인
        r1 = find_set(u)
        r2 = find_set(v)
        
        # 서로 연결이 되어 있지 않은 정점이라면
        if r1 != r2:
            # 연결시키고
            p[r1] = r2
            # 가중치를 더함
            ans += w
            cnt += 1

        if cnt == V:
            break

    print(p)
    print(f'#{tc} {ans}')



