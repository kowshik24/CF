def kor():
    t = int(input())
    for _ in range(t):
        n , m , k = map(int, input().split())
        
        num = 1
        num2 = n

        while num <= num2:
            if (num2>m):
                print(num2, end = " ")
                num2 -= 1
                
            else:
                print(num, end = " ")
                num += 1
        print()


        




if __name__ == "__main__":
    kor()