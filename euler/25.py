from collections import deque
def p2(n):
    answer = 0
    dq = deque([1, 2])
    i = dq[1]
    limit = 4_000_000
    while (i < limit):
        if (i % 2 == 0):
            answer += i
        i = dq.popleft() + dq[0]
        dq.append(i)
    print(answer)