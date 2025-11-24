def reduce_grid(t, test_cases):
    results = []
    for case in test_cases:
        n, k, grid = case
        reduced_grid_size = n // k
        reduced_grid = [[0 for _ in range(reduced_grid_size)] for _ in range(reduced_grid_size)]

        for i in range(0, n, k):
            for j in range(0, n, k):
                block_value = grid[i][j]
                consistent_block = True
                for x in range(i, i + k):
                    for y in range(j, j + k):
                        if grid[x][y] != block_value:
                            consistent_block = False
                            break
                    if not consistent_block:
                        break
                if consistent_block:
                    reduced_grid[i // k][j // k] = block_value

        results.append(reduced_grid)
    
    return results

# Read input
t = int(input())
test_cases = []
for _ in range(t):
    n, k = map(int, input().split())
    grid = [input().strip() for _ in range(n)]
    test_cases.append((n, k, grid))

# Process each test case
results = reduce_grid(t, test_cases)

# Print results
for result in results:
    for row in result:
        print("".join(row))