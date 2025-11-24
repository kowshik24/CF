def solve(n, k):
    kire = 0
    while n > 0:
        if n % 2 == 1:  
            n -= k
            kire += 1
        else:  
            
            maximum_ase = k - 1 if k % 2 == 1 else k
           
            total = n // maximum_ase
            baki_ase = n % maximum_ase
           
            kire += total
            n = baki_ase
            
            if baki_ase > 0:
                kire += 1
                n = 0
    return kire

def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        print(solve(n, k))

if __name__ == "__main__":
    main()
