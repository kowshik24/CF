import sys

def ber_kor(arr):

    s = set(arr)

    res = 0

    while res in s:
        res += 1
        
    return res

def count_kor(arr, x):

    if x == 0:
        return len(arr)
    
    lagbe = x

    freq = [0] * x

    # print(f"lagbe: {lagbe}, freq: {freq}")

    ase = 0

    count = 0

    for num in arr:
        if num < x:
            if freq[num] == 0:
                ase += 1
            freq[num] += 1
        if ase == lagbe:
            count += 1
            freq = [0] * x
            ase = 0
        # print(f"num: {num}, freq: {freq}, ase: {ase}, count: {count}")
    return count

t = int(sys.stdin.readline())
for _ in range(t):
    n, k = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    kos = ber_kor(a)
    low = 0
    high = kos
    ans = 0
    while low <= high:
        mid = (low + high) // 2
        # print(f"mid: {mid}")
        if mid == 0:
            temp = n
            # print(f"temp: {temp}")
        else:
            temp = count_kor(a, mid)
            # print(f"temp: {temp}")
        if temp >= k:
            ans = mid
            low = mid + 1
            # print(f"ans: {ans}")
            # print(f"low: {low}")
        else:
            high = mid - 1
            # print(f"high: {high}")
    print(ans)