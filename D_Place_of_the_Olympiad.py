def kor():
    t = int(input())
    
    for _ in range(t):
        n, m, k = map(int, input().split())
        
        left = 1
        right = min(k, m)
        
        while left <= right:
            mid = (left + right) // 2
            
            tot_bench = m // (mid + 1)
            baki_ase = m % (mid + 1)
            
            total = tot_bench * mid
            
            if baki_ase > 0:
                total += min(mid, baki_ase)
            
            total_parbe = n * total
            
            if total_parbe >= k:
                right = mid - 1
            else:
                left = mid + 1
        
        print(left)

kor()