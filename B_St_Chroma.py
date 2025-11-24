import sys

def kor():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, x = map(int, sys.stdin.readline().split())
        if x == 0:
            if n == 1:
                res = [0]
            else:
                res = list(range(1, n)) + [0]
        elif x == n:
            res = list(range(n))
        else:
            kos = list(range(x))
            baki_ase = list(range(x+1, n))
            res = kos + baki_ase + [x]
        print(' '.join(map(str, res)))

if __name__ == "__main__":
    kor()