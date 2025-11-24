def kire():
    n = int(input())
    a = list(map(int, input().split()))
    
    max_diff = 0
    for i in range(n):
        for j in range(i + 1, n):
            diff = abs(a[j] - a[i])
            if diff > max_diff:
                max_diff = diff
    
    return max_diff

def main():
    import sys
    input = sys.stdin.readline
    
    t = int(input())
    for _ in range(t):
        print(kire())

if __name__ == "__main__":
    main()