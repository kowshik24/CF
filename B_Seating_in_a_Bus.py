def solve(n, a):
    occupied = set()
    
    for i in range(n):
        seat = a[i]
        if i == 0:
            occupied.add(seat)
        else:
            if (seat - 1 in occupied) or (seat + 1 in occupied):
                occupied.add(seat)
            else:
                print("NO")
                return
    
    print("YES")

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    solve(n, a)