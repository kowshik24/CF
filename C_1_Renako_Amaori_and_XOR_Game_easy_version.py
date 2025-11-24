def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
   
    for i in range(n):
        if i % 2 == 0:  
                a[i], b[i] = b[i], a[i]
        else:  
            if a[i] == 1 and b[i] == 0:
                a[i], b[i] = b[i], a[i]
    
    
    ajisai_score = 0
    mai_score = 0
    
    for i in range(n):
        ajisai_score ^= a[i]
        mai_score ^= b[i]
    
    if ajisai_score > mai_score:
        print("Ajisai")
    elif mai_score > ajisai_score:
        print("Mai")
    else:
        print("Tie")

def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
