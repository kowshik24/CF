t = int(input())

while t > 0:

    n = int(input())
    x  = list(map(int, input().split()))
    sum = 10000 

    print(sum , end=" ")

    for i in range(n-1):
        sum += x[i]
        print(sum,end=" ")

    print()

    t -= 1