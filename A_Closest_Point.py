def can_add_closest_point(t, test_cases):
    results = []
    for i in range(t):
        n = test_cases[i][0]
        points = test_cases[i][1]
        
        # Calculate the minimum distance between consecutive points
        min_distance = min(points[j+1] - points[j] for j in range(n-1))
        
        # Check if we can place a new point at half of the minimum distance
        if min_distance % 2 == 0:
            new_point = points[0] + min_distance // 2
        else:
            new_point = points[0] + min_distance // 2 + 1
        
        # Ensure the new point is not already in the set and is the closest to all points
        if new_point not in points:
            distances = [abs(new_point - p) for p in points]
            if all(dist == min(distances) for dist in distances):
                results.append("YES")
            else:
                results.append("NO")
        else:
            results.append("NO")
    
    return results

# Read input
t = int(input())
test_cases = []

for _ in range(t):
    n = int(input())
    points = list(map(int, input().split()))
    test_cases.append((n, points))

# Process and print results
results = can_add_closest_point(t, test_cases)
for result in results:
    print(result)