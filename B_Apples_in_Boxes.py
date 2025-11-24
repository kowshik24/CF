import sys
input = sys.stdin.readline

def kor():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    tot = sum(a)
    kos = min(a)
    kos1 = max(a)
    baki_ase = kos1 - kos
    # print(kos1, kos)
    # print(baki_ase)
    flag = False

    if baki_ase <= k:
        flag = True
    elif baki_ase == k + 1:
        if a.count(kos1) == 1:
            flag = True
    else:
        flag = False
    
    # print(a)
    if flag:
        if tot % 2 == 1:
            print("Tom")
        else:
            print("Jerry")
    else:
        print("Jerry")

t = int(input())
for _ in range(t):
    kor()
