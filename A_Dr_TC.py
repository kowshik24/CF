def kor():
    n = int(input())
    s = input()
    res = 0
    
    
    for i in range(n):
        for j in range(n):
            if j == i:
                res += 1 if s[j] == '0' else 0
            else:
                res += 1 if s[j] == '1' else 0
                
    return res

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        print(kor())

