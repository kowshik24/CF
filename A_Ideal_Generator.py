def solve():
    t = int(input())
    for _ in range(t):
        k = int(input())
        if k == 1 or k % 2 == 1:
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    solve()
