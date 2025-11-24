def solve_bar_queue(N, S):
    boys = 0
    girls = 0
    count = 0
    
    # Process each person in the queue
    for person in S:
        if person == 'B':
            boys += 1
        else:  # person == 'G'
            girls += 1
        
        # Check if boys exceed twice the number of girls
        if boys > 2 * girls:
            break
        
        count += 1
    
    return count

# Read number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    N = int(input())
    S = input().strip()  # Read the queue string
    result = solve_bar_queue(N, S)
    print(result)