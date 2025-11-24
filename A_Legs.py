t = int(input())

while t>0:
    n = int(input())

    chicken = int(n/2)
    cows = int((n - (chicken*2))/4)

    cows_1 = int(n/4)

    chicken_1 = int((n-(cows_1*4))/2)

    print(min(chicken + cows , chicken_1 + cows_1))
    t -= 1