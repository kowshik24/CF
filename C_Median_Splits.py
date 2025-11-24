def kor():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    t = int(data[index])
    index += 1
    
    results = []
    for _ in range(t):
        n = int(data[index])
        k = int(data[index + 1])
        index += 2
        a = list(map(int, data[index:index + n]))
        index += n
        
        
        a = [0] + a
        
        cnt = [0] * (n + 1)
        for i in range(1, n + 1):
            cnt[i] = cnt[i - 1] + (1 if a[i] <= k else -1)
        
        total = cnt[n]
        flag = False
        
        
        kos1 = [float('inf')] * (n + 1)
        kos1[0] = 0  
        kos2 = [float('inf')] * (n + 1)
        kos2[0] = float('inf')  
        
        for i in range(1, n + 1):
            kos1[i] = min(kos1[i - 1], cnt[i])
            if cnt[i] >= 0:
                kos2[i] = min(kos2[i - 1], cnt[i])
            else:
                kos2[i] = kos2[i - 1]
        
        
        for i in range(2, n):
            current = cnt[i]
            
            valid_min = kos2[i - 1]
            if valid_min != float('inf') and valid_min <= current:
                flag = True
                break
            
            if valid_min != float('inf') and current <= total:
                flag = True
                break
            
            if kos1[i - 1] <= current and current <= total:
                flag = True
                break
        
        results.append("YES" if flag else "NO")
    
    print('\n'.join(results))

if __name__ == "__main__":
    kor()