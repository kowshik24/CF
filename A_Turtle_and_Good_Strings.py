
t = int(input())

while t>0:
    n = int(input())
    s = input()

    f = 0

    for i in range(n):
        if f:
            break
        for j in range(n):
            if s[i] != s[j] and s[0]!=s[n-1]:
                print("YES")
                f = 1
                break
    
    if(f == 0):
        print("NO")

    t -= 1