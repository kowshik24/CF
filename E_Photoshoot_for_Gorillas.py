def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    t = int(data[index])
    index += 1
    results = []
    
    for _ in range(t):
        n = int(data[index])
        m = int(data[index + 1])
        k = int(data[index + 2])
        index += 3
        
        w = int(data[index])
        index += 1
        
        heights = list(map(int, data[index:index + w]))
        index += w
        
        # Sort the heights in descending order
        heights.sort(reverse=True)
        
        # Initialize the grid with zeros
        grid = [[0] * m for _ in range(n)]
        
        # Place the gorillas in the grid
        idx = 0
        for i in range(n):
            for j in range(m):
                if idx < w:
                    grid[i][j] = heights[idx]
                    idx += 1
        
        # Calculate the spectacle
        max_spectacle = 0
        for i in range(n - k + 1):
            for j in range(m - k + 1):
                sub_square_sum = 0
                for x in range(k):
                    for y in range(k):
                        sub_square_sum += grid[i + x][j + y]
                max_spectacle = max(max_spectacle, sub_square_sum)
        
        results.append(max_spectacle)
    
    for result in results:
        print(result)

# Read input and solve the problem
solve()