def count_triplets(n, x):
    count = 0
    for a in range(1, x + 1):
        for b in range(1, x + 1 - a):
            for c in range(1, x + 1 - a - b):
                if a * b + b * c + c * a <= n:
                    count += 1
    return count

# Read input
t = int(input())
results = []

for _ in range(t):
    n, x = map(int, input().split())
    results.append(count_triplets(n, x))

# Print results
for result in results:
    print(result)