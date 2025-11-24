t = int(input())
for _ in range(t):
    n, a, b, c = map(int, input().split())
    
    
    cycle_distance = a + b + c
    

    if n <= a:
        print(1)
    elif n <= a + b:
        print(2)
    elif n <= cycle_distance:
        print(3)
    else:
        
        remaining = n - cycle_distance
        
        
        complete_cycles = remaining // cycle_distance
        extra = remaining % cycle_distance
        
        days = 3 + (complete_cycles * 3)
        
        
        if extra > 0:
            if extra <= a:
                days += 1
            elif extra <= a + b:
                days += 2
            else:
                days += 3
                
        print(days)
