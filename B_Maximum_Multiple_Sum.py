"""
n*(n+1)/2 * x = N
then x = N/(n*(n+1)/2)
"""

t = int(input())
for _ in range(t):
    n = int(input())
    max_x = 0
    max_sum = 0
    for x in range(2, n + 1):
        current_sum = (n // x) * (n // x + 1) * x // 2
        if current_sum > max_sum:
            max_sum = current_sum
            max_x = x
    print(max_x)