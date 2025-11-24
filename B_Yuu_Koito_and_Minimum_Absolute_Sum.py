def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    
    kos = a[0]
    kos1 = a[n-1]
    
  
    if kos == -1 and kos1 == -1:
        kos = 0
        kos1 = 0
    elif kos == -1:
        kos = kos1
    elif kos1 == -1:
        kos1 = kos
    
    
    min_diff = abs(kos1 - kos)
    print(min_diff)
    
    
    a[0] = kos
    a[n-1] = kos1
    
    
    for i in range(1, n-1):
        if a[i] == -1:
            a[i] = 0
    
    print(' '.join(map(str, a)))

def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
