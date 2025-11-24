import sys

def solve_kor(arr):
    kos = temp_max = arr[0]
    for x in arr[1:]:
        temp_max = max(x, temp_max + x)
        kos = max(kos, temp_max)
    return kos

def kor():
    n, k = map(int, sys.stdin.readline().split())
    s = sys.stdin.readline().strip()
    a = list(map(int, sys.stdin.readline().split()))

    idx = [i for i, ch in enumerate(s) if ch == '0']
    # print(len(idx))
    # print(idx)

    if not idx:
        max_sum = solve_kor(a)
        # print(max_sum)
        if max_sum == k:
            print("Yes")
            print(*a)
        else:
            print("No")
        return

    kos = float('-inf')
    curr = float('-inf')
    for i in range(n):
        if s[i] == '1':
            curr = max(a[i], (curr if curr != float('-inf') else 0) + a[i])
            # print(curr)
            kos = max(kos, curr)
            # if curr == k:
            #     idx.append(i)
            
        else:
            curr = float('-inf')

    if kos > k:
        print("No")
        return

    L = [0] * (n + 1)
    R = [0] * (n + 1)

    curr = 0
    for i in range(n):
        if s[i] == '1':
            curr = max(0, curr + a[i])
        else:
            curr = 0
        L[i + 1] = curr
    
    # print(curr)

    curr = 0
    for i in reversed(range(n)):
        if s[i] == '1':
            curr = max(0, curr + a[i])
        else:
            curr = 0
        R[i] = curr
    
    # print(curr)
    # print(L)


    p = idx[0]
    baki_ase = k - L[p] - R[p + 1]
    # print(baki_ase)

    result = a[:]
    result[p] = baki_ase
    number = -2 * 10**18
    for i in idx:
        if i != p:
            result[i] = number

    print("Yes")
    print(*result)


t = int(sys.stdin.readline())
for _ in range(t):
    kor()
