import sys

def kor():
    input = sys.stdin.read().split()
    index = 0
    t = int(input[index])
    index += 1
    for _ in range(t):
        n, k = int(input[index]), int(input[index+1])
        index +=2
        a = list(map(int, input[index:index+n]))
        index +=n
        b = list(map(int, input[index:index+n]))
        index +=n
        
        flag = True
        x = None
        for i in range(n):
            if b[i] != -1:
                curr = a[i] + b[i]
                if x is None:
                    x = curr
                else:
                    if curr != x:
                        flag = False
                        break
        
        # print(f"flag: {flag}")
        # print(f"x: {x}")

        if not flag:
            print(0)
            continue
        
        if x is not None:
            kire = True
            for i in range(n):
                if b[i] == -1:
                    baki_ase = x - a[i]
                    # print(f"baki_ase: {baki_ase}")
                    if baki_ase < 0 or baki_ase > k:
                        kire = False
                        break
            
            if kire:
                print(1)
            else:
                print(0)
        else:
            kos = max(a)
            kos1 = min(ai + k for ai in a)
            # kos1 = max(kos1, kos)
            # print(f"kos: {kos}")
            # print(f"kos1: {kos1}")
            res = kos
            res1 = kos1
            # print(f"res: {res}")
            # print(f"res1: {res1}")
            if res > res1:
                print(0)
            else:
                print(res1 - res + 1)
                
if __name__ == "__main__":
    kor()