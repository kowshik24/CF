import sys

def solve():
    input = sys.stdin.read().split()
    t = int(input[0])
    cases = list(map(int, input[1:t+1]))
    
    for n in cases:
        if n % 2 == 0:
            print(-1)
        else:
            if n == 1:
                print(1)
                continue
            shift = (n + 1) // 2
            perm = []
            for m in range(n):
                d = (m + shift) % n
                val = (m + 1 + d) % n
                perm.append(val if val != 0 else n)
            print(' '.join(map(str, perm)))

if __name__ == "__main__":
    solve()