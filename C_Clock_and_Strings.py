t = int(input())

def gcd(a , b):
    if b == 0:
        return a
    return gcd(b , a%b)

while t>0:
    a , b , c , d = map(int , input().split())

    if gcd(a , b) == 1 and  gcd(c , d)  == 1:
        print("NO")
    else:
        print("YES")
    
    t -= 1