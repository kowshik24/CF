t = int(input())


while t > 0:
    n = int(input())
    arr = list(map(int, input().split()))

    sum = 0
    for i in range(n):
        if i % 2 == 0:
            sum += arr[i]
        else:
            sum -= arr[i]

    print(sum)

    t -= 1
