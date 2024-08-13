t = int(input())

while t > 0:
    a , b = map(int , input().split())
    print(min(a , b),max(a , b))
    t -= 1