def bfs(s):
    #[0] q, v 필요한 flag 생성
    q = []
    v = [0] * 101
    ans = s

    # [1] q에 초기데이터를 삽입, v 표시
    q.append(s)
    v[s] = 1

    while q:
        #[2] q에서 한 개 꺼냄 + 필요시 정답 처리
        c = q.pop(0)
        if v[ans] < v[c] or v[ans] == v[c] and ans < c:
            ans = c


        #[3] 4/8 연결 방향 등 반복처리
        for n in adj[c]:
            if v[n] == 0:
                q.append(n)
                v[n] = v[c] + 1

    return ans


T = 10
for test_case in range(1, T+1):
    N, S = map(int, input().split())
    lst = list(map(int, input().split()))

    adj = [[] for _ in range(101)]
    for i in range(0, len(lst), 2):
        s, e = lst[i], lst[i+1]
        adj[s].append(e)

    ans = bfs(S)
    print(f'#{test_case} {ans}')