import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqrt_n = int(math.sqrt(n)) + 1
    for i in range(3, sqrt_n, 2):
        if n % i == 0:
            return False
    return True

t = int(input())
for _ in range(t):
    x, k = map(int, input().split())
    if k == 1:
        print("YES" if is_prime(x) else "NO")
    else:
        if x == 1:
            print("YES" if k == 2 else "NO")
        else:
            print("NO")