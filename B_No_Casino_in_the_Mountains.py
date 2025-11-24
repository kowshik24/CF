t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    hikes = 0
    i = 0
    
    while i <= n - k:
       
        can_start = True
        for j in range(k):
            if a[i + j] == 1:
                can_start = False
                
                i = i + j + 1
                break
        
        if can_start:
            
            hikes += 1
            
            i += k + 1
        
    
    print(hikes)
