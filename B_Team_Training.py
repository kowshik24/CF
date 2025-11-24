def kor():
    n, x = map(int, input().split())
    skills = sorted(list(map(int, input().split())), reverse=True)
    
    res = 0
    temp = 0
    temp_minimum = float('inf')
    
    for skill in skills:
        temp += 1
        temp_minimum = min(temp_minimum, skill)
        if temp * temp_minimum >= x:
            res += 1
            temp = 0
            temp_minimum = float('inf')
    
    return res

def main():
    t = int(input())
    for _ in range(t):
        print(kor())

if __name__ == "__main__":
    main()
