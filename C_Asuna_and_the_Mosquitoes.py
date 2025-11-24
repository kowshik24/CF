def kire():
    n = int(input())
    a = list(map(int, input().split()))
    
    sum_arr = sum(a)
    odd_count = sum(1 for x in a if x % 2 == 1)
    even_sum = sum(a[i] for i in range(0, n, 2))

    if odd_count == 0 or odd_count == n:
        return max(a)
    else:
        return sum_arr - (odd_count - 1)


t = int(input())

for _ in range(t):
    result = kire()
    print(result)