t = int(input())
for _ in range(t):
    n = int(input())
    if n % 2 == 0:
        print(-1)
    else:
        res = [n] + [1] + list(range(2, n))
        print(' '.join(map(str, res)))