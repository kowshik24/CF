def turtle_and_piggy_game(test_cases):
    results = []
    for case in test_cases:
        n, a = case
        # Initialize the maximum value for a1
        max_a1 = a[0]
        
        # Iterate through the array to find the maximum value for Turtle's optimal play
        for i in range(1, n):
            max_a1 = max(max_a1, a[i])
        
        # Piggy will minimize the first element
        results.append(max_a1)
    
    return results

# Read input
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    test_cases.append((n, a))

# Get results
results = turtle_and_piggy_game(test_cases)

# Print results
for result in results:
    print(result)