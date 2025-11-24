import sys

def kor():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))

    paichi = False
    for i in range(n - 1): 
        if a[i] == 0 and a[i+1] == 0:
            paichi = True
            break
    
    if paichi:
        sys.stdout.write("YES\n")
        return

    cnt = True
    for x in a:
        if x == 0:
            cnt = False
            break
    
    if cnt:
        sys.stdout.write("YES\n")
        return
        
    sys.stdout.write("NO\n")


if __name__ == "__main__":
    t = int(sys.stdin.readline())
    for _ in range(t):
        kor()