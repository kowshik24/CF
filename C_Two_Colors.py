def kor():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    
    count = 0
    
    
    for i in range(m):
        for j in range(i + 1, m):
            
            if a[i] + a[j] >= n:
               
                left = min(a[i], n - 1)
                
                count += max(0, min(left, n - 1) - max(1, n - a[j]) + 1)
            
            
            if a[j] + a[i] >= n:
               
                left = min(a[j], n - 1)
                
                count += max(0, min(left, n - 1) - max(1, n - a[i]) + 1)
    
    return count

t = int(input())
for _ in range(t):
    print(kor())