def kor():
    t = int(input())
    for _ in range(t):
        n, m, l, r = map(int, input().split())
        num1 = min(m, r)  
        num2 = num1 - m   
        print(num2, num1)

if __name__ == "__main__":
    kor()
