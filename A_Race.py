def solve():
    a, x, y = map(int, input().split())
    
    p_min = min(x, y)
    p_max = max(x, y)
    
    if a > p_min and a < p_max:
        print("NO")
    else:
        print("YES")


if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        solve()

