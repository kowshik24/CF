t = int(input())

while t:
    x1 , x2 , x3 = map(int, input().split())
    num1 = abs(x1-x2)
    num2 = abs(x2-x3)
    num3 = max(num1, num2, abs(x1-x3))
    print(num3)
    t -= 1
