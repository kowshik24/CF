def solve():
    import sys
    data = sys.stdin.read().strip().split()
    t = int(data[0])
    idx = 1
    
    
    def no_overlap(a, b):
        return (a & b) == 0
    
    for _ in range(t):
        x = int(data[idx])
        y = int(data[idx + 1])
        idx += 2
        
        
        if no_overlap(x, y):
            print(0)
            continue
        
        k = 0
        found = False
        
        
        while True:
            if no_overlap(x + k, y + k):
                print(k)
                found = True
                break
            
            overlap = (x + k) & (y + k)
            lowest_bit = overlap & -overlap
            increment = lowest_bit - ((x + k) & (lowest_bit - 1))
            k += increment
            
            if k > 10**18:
                break
        
        if not found:
            print(-1)

if __name__ == "__main__":
    solve()