def kos(n, k, arr):
    
    maxi_cost = 0
    
    
    for idx in range(n):
       
        baki_indices = [i for i in range(n) if i != idx]
        
        
        baki_indices.sort(key=lambda i: -arr[i])
        
       
        first = baki_indices[:k]
        
        
        
        colored = set(first)
        queue = list(first)
        
        
        while queue:
            current = queue.pop(0)
            
            
            for neighbor in [current - 1, current + 1]:
                if 0 <= neighbor < n and neighbor not in colored and neighbor != idx:
                    colored.add(neighbor)
                    queue.append(neighbor)
        
        
        final = all(i in colored for i in range(n) if i != idx)
        
        
        pasher_color = (idx > 0 and idx - 1 in colored) or (idx < n - 1 and idx + 1 in colored)
        
        
        if final and pasher_color:
            cost = sum(arr[i] for i in first) + arr[idx]
            maxi_cost = max(maxi_cost, cost)
    
    return maxi_cost

def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        arr = list(map(int, input().split()))
        print(kos(n, k, arr))

if __name__ == "__main__":
    main()