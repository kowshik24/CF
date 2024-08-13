t = int(input())

while t > 0:
    n, s, m = map(int, input().split())
    time_map = {}
    start_time = 0
    f = 0

    for i in range(n):
        a = list(map(int, input().split()))
        time_map[i] = (a[0], a[1])
        if i == 0:
            if a[0] - start_time >= s:
                f = 1
        else:
            if time_map[i][0] - time_map[i-1][1] >= s:
                f = 1

    if f == 1 or m - time_map[n-1][1] >= s:
        print("YES")
    else:
        print("NO")

    t -= 1