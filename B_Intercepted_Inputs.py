def find_grid_dimensions():
    import math
    t = int(input())  
    results = []
    
    for _ in range(t):
        k = int(input())  
        a = list(map(int, input().split()))  
        
        
        possible_dimensions = []
        for i in range(1, int(math.sqrt(k)) + 1):
            if k % i == 0:
                possible_dimensions.append((i, k // i)) 
                possible_dimensions.append((k // i, i))  

        
        for n, m in possible_dimensions:
            if n in a and m in a:  
                results.append((n, m))
                break

    
    for n, m in results:
        print(n, m)


find_grid_dimensions()
