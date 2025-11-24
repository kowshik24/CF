import math
import sys

def gcd_kor(kos):
    if len(kos) == 1:
        return kos[0]
    res = kos[0]
    for i in range(1, len(kos)):
        res = math.gcd(res, kos[i])
    return res

def kor():
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))

    if len(set(arr)) == 1:
        print("No")
        return

    print("Yes")

    min_val = arr[0]
    min_idx = 0
    for i in range(1, n):
        if arr[i] < min_val:
            min_val = arr[i]
            min_idx = i

    kos = []
    for i in range(n):
        if i != min_idx:
            kos.append(arr[i])

    g2 = gcd_kor(kos)
    g1 = arr[min_idx]

    if g1 != g2:
        ans = [2] * n
        ans[min_idx] = 1
        print(*ans)
    else:
        p = -1
        for i in range(n):
            if arr[i] != min_val:
                p = i
                break
        ans = [2] * n
        ans[p] = 1
        print(*ans)

t = int(sys.stdin.readline())
for _ in range(t):
    kor()
