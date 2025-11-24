def kor():
    t = int(input())
    for _ in range(t):
        n , k = map(int, input().split())
        if k%2 == 1:
            s = ""
            for i in range(n-1):
                # print(str(n) + "")
                s += str(n) + " "
            s += str(n-1)
            print(s)
            # print(str(n-1) + " ")
        else:
            # n-1 , n-1 , n-1 , n , n-1
            s = ""
            for i in range(n-2):
                # print(n-1)
                s += str(n-1) + " "
            s += str(n) + " " + str(n-1)
            print(s)
            # print(n-1)
            # print(n)
            # print(n-1)
kor()