t = int(input())

while t > 0:
    n , m = map(int, input().split())
    a = input()
    b = input()

    k = 0
    for i in range(m):
        if k < n and a[k] == b[i]:
            k += 1
    
    print(k)

    t -= 1


