t = int(input())

while t > 0:
    n = int(input())
    number_string = str(n)

    sum = 0

    for i in range(0,len(number_string)):
        sum += int(number_string[i])
    
    print(sum)
    t -=1 