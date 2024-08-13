t = int(input())


while t>0:
    s = input()
    f = 1
    for i in range(len(s)-1):
        if s[i] != s[i+1]:
            f = 0
            break
    if f:
        print("NO")
    else:
        print("YES")
        print(s[::-1])
    
    t -= 1