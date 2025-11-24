t = int(input())
for _ in range(t):
    n = input().strip()
    res = 0
    baki_ase = 0
    for c in n:
        if c == '0':
            baki_ase += 1
        else:
            current_len = baki_ase + 1
            if current_len > res:
                res = current_len
    print(len(n) - res)