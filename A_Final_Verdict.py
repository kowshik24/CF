def kor():
    t = int(input())
    for  _ in range(t):
        n , x = map(int,input().split())
        a = list(map(int,input().split()))

        sum = 0
        for i in range(n):
            sum += a[i]
        
        if n * x == sum:
            print("YES")
        else:
            print("NO")
kor()